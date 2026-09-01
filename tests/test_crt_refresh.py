from __future__ import annotations

import runpy
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CRT_REFRESH = runpy.run_path(
    ROOT / "experiments" / "crt-refresh" / "crt_refresh.py"
)
simulate = CRT_REFRESH["simulate"]


class CrtRefreshTests(unittest.TestCase):
    def test_scan_capacity_is_accumulated_across_refresh_ticks(self) -> None:
        for seconds, scan_capacity, expected_operations in (
            (1.0, 10.0, 10),
            (1.0, 25.0, 25),
            (1.0, 30.0, 30),
            (1.0, 8_000.0, 8_000),
            (2.0, 2.0, 4),
        ):
            with self.subTest(seconds=seconds, scan_capacity=scan_capacity):
                result = simulate(
                    cells=128,
                    seconds=seconds,
                    refreshes_per_second=20.0,
                    scan_capacity_per_second=scan_capacity,
                    decay_per_second=0.0,
                )

                self.assertEqual(result.refresh_operations, expected_operations)

    def test_decimal_rate_ratio_does_not_miss_an_exact_boundary(self) -> None:
        result = simulate(
            cells=3,
            seconds=5.0,
            refreshes_per_second=0.7,
            scan_capacity_per_second=0.7,
            decay_per_second=0.0,
        )

        self.assertEqual(result.refresh_operations, 3)

    def test_cumulative_capacity_is_floored_at_each_tick(self) -> None:
        for seconds, expected_operations in (
            (0.5, 1),
            (1.0, 3),
            (1.5, 4),
            (2.0, 6),
        ):
            with self.subTest(seconds=seconds):
                result = simulate(
                    cells=8,
                    seconds=seconds,
                    refreshes_per_second=2.0,
                    scan_capacity_per_second=3.0,
                    decay_per_second=0.0,
                )

                self.assertEqual(result.refresh_operations, expected_operations)

    def test_decimal_boundary_refresh_happens_before_signal_is_lost(self) -> None:
        result = simulate(
            cells=3,
            seconds=6.0,
            refreshes_per_second=0.7,
            scan_capacity_per_second=0.7,
            decay_per_second=0.175,
            threshold=0.25,
        )

        self.assertEqual(result.refresh_operations, 4)
        self.assertEqual(result.lost_cells, 0)


if __name__ == "__main__":
    unittest.main()
