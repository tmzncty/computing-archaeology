from __future__ import annotations

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "experiments" / "carry-propagation" / "carry_propagation.py"
SPEC = importlib.util.spec_from_file_location("carry_propagation", SCRIPT)
if SPEC is None or SPEC.loader is None:  # pragma: no cover - importlib contract
    raise RuntimeError(f"could not load {SCRIPT}")
CARRY_PROPAGATION = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = CARRY_PROPAGATION
SPEC.loader.exec_module(CARRY_PROPAGATION)


class DigitCapacityTests(unittest.TestCase):
    def test_exact_power_boundaries_across_radices(self) -> None:
        for radix in (2, 3, 5, 10, 16, 36):
            for exponent in range(1, 19):
                power = radix**exponent
                cases = (
                    (power - 2, exponent),
                    (power - 1, exponent),
                    (power, exponent + 1),
                )
                for max_value, expected in cases:
                    with self.subTest(
                        radix=radix,
                        exponent=exponent,
                        max_value=max_value,
                    ):
                        self.assertEqual(
                            CARRY_PROPAGATION.digits_required(max_value, radix),
                            expected,
                        )

    def test_zero_one_and_invalid_inputs(self) -> None:
        self.assertEqual(CARRY_PROPAGATION.digits_required(0, 2), 1)
        self.assertEqual(CARRY_PROPAGATION.digits_required(1, 36), 1)

        with self.assertRaisesRegex(ValueError, "max_value must be non-negative"):
            CARRY_PROPAGATION.digits_required(-1, 10)
        for radix in (0, 1):
            with self.subTest(radix=radix):
                with self.assertRaisesRegex(ValueError, "radix must be at least 2"):
                    CARRY_PROPAGATION.digits_required(10, radix)

    def test_large_integer_boundary_does_not_require_float_conversion(self) -> None:
        self.assertEqual(CARRY_PROPAGATION.digits_required(10**400, 10), 401)
        self.assertEqual(CARRY_PROPAGATION.digits_required(36**400 - 1, 36), 400)

    def test_simulation_and_cli_report_correct_boundary_capacity(self) -> None:
        result = CARRY_PROPAGATION.simulate(radix=5, max_value=124, increments=1)
        self.assertEqual(result.digits_for_range, 3)

        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--max-value",
                "124",
                "--increments",
                "1",
                "--radices",
                "5",
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        rows = [line.split() for line in completed.stdout.splitlines()]
        radix_row = next(row for row in rows if row[:1] == ["5"])
        self.assertEqual(radix_row[:2], ["5", "3"])


if __name__ == "__main__":
    unittest.main()
