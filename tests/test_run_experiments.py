from __future__ import annotations

import io
import math
import os
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import Mock, call, patch

from tools.run_experiments import (
    DiscoveryError,
    _MAX_WAIT_SLICE_SECONDS,
    _cleanup_process_tree,
    _start_experiment,
    discover_experiments,
    main,
    run_experiments,
)


class ExperimentRunnerTests(unittest.TestCase):
    def make_experiment(self, root: Path, name: str, source: str) -> Path:
        directory = root / "experiments" / name
        directory.mkdir(parents=True)
        script = directory / f"{name.replace('-', '_')}.py"
        script.write_text(source, encoding="utf-8")
        return script

    def make_descendant_experiment(
        self,
        root: Path,
        name: str,
        parent_sleep: float,
    ) -> tuple[Path, Path, Path]:
        ready = root / f"{name}-grandchild-ready.txt"
        finished = root / f"{name}-grandchild-finished.txt"
        grandchild_source = (
            "from pathlib import Path\n"
            "import sys\n"
            "import time\n"
            "ready = Path(sys.argv[1])\n"
            "finished = Path(sys.argv[2])\n"
            "ready.write_text(str(time.monotonic()), encoding='utf-8')\n"
            "time.sleep(2.0)\n"
            "finished.write_text('survived', encoding='utf-8')\n"
        )
        script = self.make_experiment(
            root,
            name,
            "import subprocess\n"
            "import sys\n"
            "import time\n"
            f"grandchild_source = {grandchild_source!r}\n"
            "subprocess.Popen(\n"
            "    [\n"
            "        sys.executable,\n"
            "        '-c',\n"
            "        grandchild_source,\n"
            f"        {str(ready)!r},\n"
            f"        {str(finished)!r},\n"
            "    ]\n"
            ")\n"
            f"time.sleep({parent_sleep!r})\n",
        )
        return script, ready, finished

    def assert_descendant_was_terminated(
        self,
        ready: Path,
        finished: Path,
    ) -> None:
        self.assertTrue(ready.exists(), "grandchild did not start before timeout")
        ready_at = float(ready.read_text(encoding="utf-8"))
        time.sleep(max(0.0, ready_at + 2.5 - time.monotonic()))
        self.assertFalse(
            finished.exists(),
            "experiment cleanup left a descendant process running",
        )

    def test_new_failing_experiment_is_discovered_and_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            passing = self.make_experiment(root, "existing", "raise SystemExit(0)\n")
            failing = self.make_experiment(root, "new-experiment", "raise SystemExit(17)\n")

            scripts = discover_experiments(root)
            failures = run_experiments(root, scripts)

            self.assertEqual(scripts, [passing, failing])
            self.assertEqual(
                failures,
                [(failing.relative_to(root), 17)],
            )

    def test_ambiguous_experiment_entry_points_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.make_experiment(root, "ambiguous", "raise SystemExit(0)\n")
            second = root / "experiments" / "ambiguous" / "helper.py"
            second.write_text("VALUE = 1\n", encoding="utf-8")

            with self.assertRaisesRegex(
                DiscoveryError,
                "expected exactly one Python entry point, found 2",
            ):
                discover_experiments(root)

    def test_timed_out_experiment_is_reported_and_later_scripts_continue(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            stalled, ready, finished = self.make_descendant_experiment(
                root,
                "stalled",
                parent_sleep=60.0,
            )
            failing = self.make_experiment(
                root,
                "later-failure",
                "raise SystemExit(17)\n",
            )

            failures = run_experiments(
                root,
                [stalled, failing],
                timeout_seconds=1.0,
            )

            self.assertEqual(
                failures,
                [
                    (stalled.relative_to(root), None),
                    (failing.relative_to(root), 17),
                ],
            )
            self.assert_descendant_was_terminated(ready, finished)

    def test_tree_cleanup_survives_the_parent_exiting_after_timeout(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            script, ready, finished = self.make_descendant_experiment(
                root,
                "parent-race",
                parent_sleep=0.5,
            )
            process = _start_experiment(root, script)
            try:
                with self.assertRaises(subprocess.TimeoutExpired):
                    process.wait(timeout=0.1)
                self.assertEqual(process.wait(timeout=2.0), 0)
            finally:
                _cleanup_process_tree(process)

            self.assert_descendant_was_terminated(ready, finished)

    def test_timeout_must_be_positive_and_finite(self) -> None:
        for value in (0.0, -1.0, math.nan, math.inf, -math.inf):
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "positive finite"):
                    run_experiments(Path.cwd(), [], timeout_seconds=value)

    def test_large_timeout_waits_in_slices_until_process_finishes(self) -> None:
        root = Path.cwd()
        script = root / "quick.py"
        process = Mock(args=["quick.py"])
        process.wait.side_effect = [
            subprocess.TimeoutExpired(process.args, _MAX_WAIT_SLICE_SECONDS),
            0,
        ]

        with (
            patch("tools.run_experiments._start_experiment", return_value=process),
            patch("tools.run_experiments._cleanup_process_tree") as cleanup,
            patch(
                "tools.run_experiments.time.monotonic",
                side_effect=[100.0, 100.0 + _MAX_WAIT_SLICE_SECONDS],
            ),
        ):
            failures = run_experiments(
                root,
                [script],
                timeout_seconds=3 * _MAX_WAIT_SLICE_SECONDS,
            )

        self.assertEqual(failures, [])
        self.assertEqual(
            process.wait.call_args_list,
            [
                call(timeout=_MAX_WAIT_SLICE_SECONDS),
                call(timeout=_MAX_WAIT_SLICE_SECONDS),
            ],
        )
        cleanup.assert_called_once_with(process)

    def test_cleanup_starts_only_after_the_configured_deadline(self) -> None:
        root = Path.cwd()
        script = root / "stalled.py"
        process = Mock(args=["stalled.py"])
        events: list[tuple[str, float | None]] = []

        def wait(timeout: float) -> int:
            events.append(("wait", timeout))
            raise subprocess.TimeoutExpired(process.args, timeout)

        def cleanup(_: object) -> None:
            events.append(("cleanup", None))

        process.wait.side_effect = wait
        timeout_seconds = 2 * _MAX_WAIT_SLICE_SECONDS
        with (
            patch("tools.run_experiments._start_experiment", return_value=process),
            patch("tools.run_experiments._cleanup_process_tree", side_effect=cleanup),
            patch(
                "tools.run_experiments.time.monotonic",
                side_effect=[
                    100.0,
                    100.0 + _MAX_WAIT_SLICE_SECONDS,
                    100.0 + timeout_seconds,
                ],
            ),
        ):
            failures = run_experiments(
                root,
                [script],
                timeout_seconds=timeout_seconds,
            )

        self.assertEqual(failures, [(Path("stalled.py"), None)])
        self.assertEqual(
            events,
            [
                ("wait", _MAX_WAIT_SLICE_SECONDS),
                ("wait", _MAX_WAIT_SLICE_SECONDS),
                ("cleanup", None),
            ],
        )

    def test_finished_process_is_not_timed_out_by_a_large_budget(self) -> None:
        root = Path.cwd()
        script = root / "quick.py"
        process = Mock(args=["quick.py"])
        process.wait.return_value = 0

        with (
            patch("tools.run_experiments._start_experiment", return_value=process),
            patch("tools.run_experiments._cleanup_process_tree") as cleanup,
            patch(
                "tools.run_experiments.time.monotonic",
                return_value=100.0,
            ),
        ):
            failures = run_experiments(
                root,
                [script],
                timeout_seconds=sys.float_info.max,
            )

        self.assertEqual(failures, [])
        process.wait.assert_called_once_with(timeout=_MAX_WAIT_SLICE_SECONDS)
        cleanup.assert_called_once_with(process)

    @unittest.skipUnless(os.name == "nt", "Windows wait boundary")
    def test_windows_wait_does_not_wrap_large_finite_timeout(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            quick = self.make_experiment(root, "quick", "pass\n")

            failures = run_experiments(
                root,
                [quick],
                timeout_seconds=(2**32) / 1000,
            )

            self.assertEqual(failures, [])

    @unittest.skipUnless(os.name == "nt", "Windows wait boundary")
    def test_windows_wait_does_not_overflow_huge_finite_timeout(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            quick = self.make_experiment(root, "quick", "pass\n")

            failures = run_experiments(
                root,
                [quick],
                timeout_seconds=1e308,
            )

            self.assertEqual(failures, [])

    def test_cli_reports_the_timeout_and_returns_failure(self) -> None:
        stalled = Path("experiments") / "stalled" / "stalled.py"
        with (
            patch(
                "tools.run_experiments.discover_experiments",
                return_value=[stalled],
            ),
            patch(
                "tools.run_experiments.run_experiments",
                return_value=[(stalled, None)],
            ) as run,
            patch("sys.stderr", new_callable=io.StringIO) as stderr,
        ):
            result = main(["--timeout-seconds", "2.5"])

        self.assertEqual(result, 1)
        self.assertEqual(run.call_args.args[1:], ([stalled], 2.5))
        self.assertEqual(
            stderr.getvalue(),
            "Experiment smoke-test failures:\n"
            f"  {stalled} (timed out after 2.5 seconds)\n",
        )


if __name__ == "__main__":
    unittest.main()
