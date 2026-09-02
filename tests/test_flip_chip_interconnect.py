from __future__ import annotations

import importlib.util
import math
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "experiments" / "flip-chip-interconnect" / "flip_chip_interconnect.py"
SPEC = importlib.util.spec_from_file_location("flip_chip_interconnect", SCRIPT)
if SPEC is None or SPEC.loader is None:  # pragma: no cover - importlib contract
    raise RuntimeError(f"could not load {SCRIPT}")
FLIP_CHIP = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = FLIP_CHIP
SPEC.loader.exec_module(FLIP_CHIP)


class FlipChipInterconnectTests(unittest.TestCase):
    def test_exact_decimal_pitch_boundaries_are_not_lost(self) -> None:
        for side, pitch, expected_perimeter, expected_area in (
            (10.0, 0.1, 400, 10_000),
            (2.0, 0.2, 40, 100),
            (0.6, 0.02, 120, 900),
            (0.3, 0.1, 12, 9),
        ):
            with self.subTest(side=side, pitch=pitch):
                self.assertEqual(
                    FLIP_CHIP.perimeter_sites(side, pitch), expected_perimeter
                )
                self.assertEqual(FLIP_CHIP.area_sites(side, pitch), expected_area)

    def test_nextafter_values_stay_on_their_side_of_the_boundary(self) -> None:
        below = math.nextafter(0.3, 0.0)
        above = math.nextafter(0.3, math.inf)
        for side, expected_perimeter, expected_area in (
            (below, 11, 4),
            (0.3, 12, 9),
            (above, 12, 9),
        ):
            with self.subTest(side=side):
                self.assertEqual(
                    FLIP_CHIP.perimeter_sites(side, 0.1), expected_perimeter
                )
                self.assertEqual(FLIP_CHIP.area_sites(side, 0.1), expected_area)

    def test_partial_pitch_is_floored_without_a_tolerance(self) -> None:
        for side, pitch, expected_perimeter, expected_area in (
            (0.29, 0.1, 11, 4),
            (1.0, 0.3, 13, 9),
            (0.29999999999, 0.1, 11, 4),
        ):
            with self.subTest(side=side, pitch=pitch):
                self.assertEqual(
                    FLIP_CHIP.perimeter_sites(side, pitch), expected_perimeter
                )
                self.assertEqual(FLIP_CHIP.area_sites(side, pitch), expected_area)

    def test_two_decimal_measurement_grid_matches_integer_geometry(self) -> None:
        for side_tenths in range(1, 101):
            side = side_tenths / 10
            for pitch_hundredths in range(1, 101):
                pitch = pitch_hundredths / 100
                positions_per_side = (10 * side_tenths) // pitch_hundredths
                expected_perimeter = (40 * side_tenths) // pitch_hundredths
                expected_area = positions_per_side * positions_per_side
                case = f"side={side}, pitch={pitch}"

                self.assertEqual(
                    FLIP_CHIP.perimeter_sites(side, pitch),
                    expected_perimeter,
                    case,
                )
                self.assertEqual(FLIP_CHIP.area_sites(side, pitch), expected_area, case)

    def test_nonpositive_and_nonfinite_measurements_are_rejected(self) -> None:
        invalid_values = (
            ("zero", 0.0),
            ("negative zero", -0.0),
            ("negative", -1.0),
            ("NaN", math.nan),
            ("positive infinity", math.inf),
            ("negative infinity", -math.inf),
        )
        for function in (FLIP_CHIP.area_sites, FLIP_CHIP.perimeter_sites):
            for parameter in ("side_mm", "pitch_mm"):
                for label, invalid in invalid_values:
                    with self.subTest(
                        function=function.__name__,
                        parameter=parameter,
                        invalid=label,
                    ):
                        arguments = (
                            (invalid, 0.1) if parameter == "side_mm" else (1.0, invalid)
                        )
                        with self.assertRaises(ValueError) as raised:
                            function(*arguments)
                        self.assertEqual(
                            str(raised.exception),
                            f"{parameter} must be finite and strictly positive",
                        )

    def test_default_output_is_unchanged(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-B", str(SCRIPT)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertEqual(
            completed.stdout,
            "Synthetic 10.0 mm square die\n"
            "pitch=1.00 mm  perimeter~  40  area-array~  100\n"
            "pitch=0.50 mm  perimeter~  80  area-array~  400\n"
            "pitch=0.25 mm  perimeter~ 160  area-array~ 1600\n",
        )


if __name__ == "__main__":
    unittest.main()
