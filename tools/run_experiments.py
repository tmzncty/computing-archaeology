#!/usr/bin/env python3
"""Discover and execute every experiment's default non-interactive path."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


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


def run_experiments(
    root: Path, scripts: list[Path]
) -> list[tuple[Path, int]]:
    """Run every entry point and return all non-zero exit codes."""
    failures: list[tuple[Path, int]] = []
    total = len(scripts)

    for index, script in enumerate(scripts, start=1):
        relative = script.relative_to(root)
        print(f"[{index}/{total}] {relative}", flush=True)
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=root,
            check=False,
        )
        if result.returncode:
            failures.append((relative, result.returncode))

    return failures


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    try:
        scripts = discover_experiments(root)
    except DiscoveryError as exc:
        print(f"Experiment discovery failed:\n{exc}", file=sys.stderr)
        return 2

    failures = run_experiments(root, scripts)
    if failures:
        print("Experiment smoke-test failures:", file=sys.stderr)
        for path, returncode in failures:
            print(f"  {path} (exit {returncode})", file=sys.stderr)
        return 1

    print(f"Experiment smoke tests: {len(scripts)} passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
