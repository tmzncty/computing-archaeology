#!/usr/bin/env python3
"""Discover and execute every experiment's default non-interactive path."""

from __future__ import annotations

import argparse
import math
import os
import signal
import subprocess
import sys
import time
from pathlib import Path


DEFAULT_TIMEOUT_SECONDS = 15.0
_MAX_WAIT_SLICE_SECONDS = 24 * 60 * 60


if os.name == "nt":
    import ctypes
    from ctypes import wintypes

    _JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE = 0x00002000
    _JOB_OBJECT_EXTENDED_LIMIT_INFORMATION_CLASS = 9

    class _JobObjectBasicLimitInformation(ctypes.Structure):
        _fields_ = [
            ("PerProcessUserTimeLimit", ctypes.c_int64),
            ("PerJobUserTimeLimit", ctypes.c_int64),
            ("LimitFlags", wintypes.DWORD),
            ("MinimumWorkingSetSize", ctypes.c_size_t),
            ("MaximumWorkingSetSize", ctypes.c_size_t),
            ("ActiveProcessLimit", wintypes.DWORD),
            ("Affinity", ctypes.c_size_t),
            ("PriorityClass", wintypes.DWORD),
            ("SchedulingClass", wintypes.DWORD),
        ]

    class _IoCounters(ctypes.Structure):
        _fields_ = [
            ("ReadOperationCount", ctypes.c_uint64),
            ("WriteOperationCount", ctypes.c_uint64),
            ("OtherOperationCount", ctypes.c_uint64),
            ("ReadTransferCount", ctypes.c_uint64),
            ("WriteTransferCount", ctypes.c_uint64),
            ("OtherTransferCount", ctypes.c_uint64),
        ]

    class _JobObjectExtendedLimitInformation(ctypes.Structure):
        _fields_ = [
            ("BasicLimitInformation", _JobObjectBasicLimitInformation),
            ("IoInfo", _IoCounters),
            ("ProcessMemoryLimit", ctypes.c_size_t),
            ("JobMemoryLimit", ctypes.c_size_t),
            ("PeakProcessMemoryUsed", ctypes.c_size_t),
            ("PeakJobMemoryUsed", ctypes.c_size_t),
        ]

    _kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    _kernel32.CreateJobObjectW.argtypes = [wintypes.LPVOID, wintypes.LPCWSTR]
    _kernel32.CreateJobObjectW.restype = wintypes.HANDLE
    _kernel32.SetInformationJobObject.argtypes = [
        wintypes.HANDLE,
        ctypes.c_int,
        wintypes.LPVOID,
        wintypes.DWORD,
    ]
    _kernel32.SetInformationJobObject.restype = wintypes.BOOL
    _kernel32.GetCurrentProcess.argtypes = []
    _kernel32.GetCurrentProcess.restype = wintypes.HANDLE
    _kernel32.AssignProcessToJobObject.argtypes = [
        wintypes.HANDLE,
        wintypes.HANDLE,
    ]
    _kernel32.AssignProcessToJobObject.restype = wintypes.BOOL
    _kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
    _kernel32.CloseHandle.restype = wintypes.BOOL


class DiscoveryError(ValueError):
    """Raised when the experiment tree has no unambiguous entry points."""


def discover_experiments(root: Path) -> list[Path]:
    """Return one Python entry point per immediate experiment directory."""
    experiment_root = root / "experiments"
    if not experiment_root.is_dir():
        raise DiscoveryError(f"missing experiment directory: {experiment_root}")

    scripts: list[Path] = []
    problems: list[str] = []
    directories = sorted(
        (
            path
            for path in experiment_root.iterdir()
            if path.is_dir()
            and path.name != "__pycache__"
            and not path.name.startswith(".")
        ),
        key=lambda path: path.name,
    )

    for directory in directories:
        candidates = sorted(
            path for path in directory.glob("*.py") if path.is_file()
        )
        if len(candidates) != 1:
            problems.append(
                f"{directory.relative_to(root)}: expected exactly one Python "
                f"entry point, found {len(candidates)}"
            )
            continue
        scripts.append(candidates[0])

    if problems:
        raise DiscoveryError("\n".join(problems))
    if not scripts:
        raise DiscoveryError("no experiment entry points found")
    return scripts


def _create_windows_kill_on_close_job() -> object:
    job_handle = _kernel32.CreateJobObjectW(None, None)
    if not job_handle:
        raise ctypes.WinError(ctypes.get_last_error())

    limits = _JobObjectExtendedLimitInformation()
    limits.BasicLimitInformation.LimitFlags = _JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
    configured = _kernel32.SetInformationJobObject(
        job_handle,
        _JOB_OBJECT_EXTENDED_LIMIT_INFORMATION_CLASS,
        ctypes.byref(limits),
        ctypes.sizeof(limits),
    )
    if not configured:
        error = ctypes.WinError(ctypes.get_last_error())
        _kernel32.CloseHandle(job_handle)
        raise error
    return job_handle


def _run_windows_contained_experiment(script: Path) -> int:
    """Run one script from a process that owns its descendants' Job Object."""
    job_handle = _create_windows_kill_on_close_job()
    current_process = _kernel32.GetCurrentProcess()
    if not _kernel32.AssignProcessToJobObject(job_handle, current_process):
        error = ctypes.WinError(ctypes.get_last_error())
        _kernel32.CloseHandle(job_handle)
        raise error

    # This process intentionally keeps the only job handle open until it exits.
    # Whether the target returns or this wrapper is killed on timeout, Windows
    # then closes the handle and terminates every descendant in the job.
    result = subprocess.run(
        [sys.executable, str(script)],
        check=False,
    )
    return result.returncode


def _start_experiment(
    root: Path,
    script: Path,
) -> subprocess.Popen[object]:
    if os.name == "nt":
        return subprocess.Popen(
            [
                sys.executable,
                str(Path(__file__).resolve()),
                "--_contained-experiment",
                str(script.resolve()),
            ],
            cwd=root,
        )
    return subprocess.Popen(
        [sys.executable, str(script)],
        cwd=root,
        start_new_session=True,
    )


def _cleanup_process_tree(
    process: subprocess.Popen[object],
) -> None:
    cleanup_error: OSError | None = None
    if os.name != "nt":
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        except OSError as error:
            cleanup_error = error

    if process.poll() is None:
        process.kill()
    process.wait()
    if cleanup_error is not None:
        raise cleanup_error


def _wait_for_process(
    process: subprocess.Popen[object],
    timeout_seconds: float,
) -> int:
    """Wait to the configured deadline without overflowing platform waits."""
    deadline = time.monotonic() + timeout_seconds
    remaining = timeout_seconds
    while True:
        # Windows wait APIs accept a 32-bit millisecond count. Keeping every
        # individual wait well inside that range prevents large finite budgets
        # from wrapping or overflowing while preserving the full deadline.
        wait_slice = min(remaining, _MAX_WAIT_SLICE_SECONDS)
        try:
            return process.wait(timeout=wait_slice)
        except subprocess.TimeoutExpired:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise subprocess.TimeoutExpired(
                    process.args,
                    timeout_seconds,
                ) from None


def run_experiments(
    root: Path,
    scripts: list[Path],
    timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
) -> list[tuple[Path, int | None]]:
    """Run every entry point, returning ``None`` for a timed-out process."""
    if not math.isfinite(timeout_seconds) or timeout_seconds <= 0:
        raise ValueError("timeout_seconds must be a positive finite number")

    failures: list[tuple[Path, int | None]] = []
    total = len(scripts)

    for index, script in enumerate(scripts, start=1):
        relative = script.relative_to(root)
        print(f"[{index}/{total}] {relative}", flush=True)
        process = _start_experiment(root, script)
        timed_out = False
        try:
            returncode = _wait_for_process(process, timeout_seconds)
        except subprocess.TimeoutExpired:
            timed_out = True
            returncode = None
        finally:
            _cleanup_process_tree(process)

        if timed_out:
            failures.append((relative, None))
            continue
        if returncode:
            failures.append((relative, returncode))

    return failures


def positive_finite_seconds(raw: str) -> float:
    """Parse a positive finite duration for argparse."""
    try:
        value = float(raw)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("must be a number") from exc
    if not math.isfinite(value) or value <= 0:
        raise argparse.ArgumentTypeError("must be a positive finite number")
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Run every experiment's default non-interactive path."
    )
    parser.add_argument(
        "--_contained-experiment",
        type=Path,
        help=argparse.SUPPRESS,
    )
    parser.add_argument(
        "--timeout-seconds",
        type=positive_finite_seconds,
        default=DEFAULT_TIMEOUT_SECONDS,
        help=(
            "maximum runtime for each experiment "
            f"(default: {DEFAULT_TIMEOUT_SECONDS:g})"
        ),
    )
    args = parser.parse_args(argv)

    if args._contained_experiment is not None:
        if os.name != "nt":
            parser.error("the contained-experiment bootstrap is Windows-only")
        return _run_windows_contained_experiment(args._contained_experiment)

    root = Path(__file__).resolve().parents[1]
    try:
        scripts = discover_experiments(root)
    except DiscoveryError as exc:
        print(f"Experiment discovery failed:\n{exc}", file=sys.stderr)
        return 2

    failures = run_experiments(root, scripts, args.timeout_seconds)
    if failures:
        print("Experiment smoke-test failures:", file=sys.stderr)
        for path, returncode in failures:
            if returncode is None:
                detail = f"timed out after {args.timeout_seconds:g} seconds"
            else:
                detail = f"exit {returncode}"
            print(f"  {path} ({detail})", file=sys.stderr)
        return 1

    print(f"Experiment smoke tests: {len(scripts)} passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
