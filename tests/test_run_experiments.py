from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.run_experiments import (
    DiscoveryError,
    discover_experiments,
    run_experiments,
)


class ExperimentRunnerTests(unittest.TestCase):
    def make_experiment(self, root: Path, name: str, source: str) -> Path:
        directory = root / "experiments" / name
        directory.mkdir(parents=True)
        script = directory / f"{name.replace('-', '_')}.py"
        script.write_text(source, encoding="utf-8")
        return script

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


if __name__ == "__main__":
    unittest.main()
