from __future__ import annotations

import runpy
import unittest
from math import nextafter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CRT_REFRESH = runpy.run_path(
    ROOT / "experiments" / "crt-refresh" / "crt_refresh.py"
)
simulate = CRT_REFRESH["simulate"]


class CrtRefreshTests(unittest.TestCase):
    def test_decimal_duration_keeps_every_complete_tick(self) -> None:
        for seconds, rate, expected_operations in (
            (0.29, 100.0, 29),
            (0.57, 100.0, 57),
            (2.9, 10.0, 29),
            (0.58, 50.0, 29),
        ):
            with self.subTest(seconds=seconds, rate=rate):
                result = simulate(1, seconds, rate, rate, 0.0)
                self.assertEqual(result.refresh_operations, expected_operations)

    def test_partial_duration_is_floored_not_rounded(self) -> None:
        for seconds, expected_operations in (
            (nextafter(0.29, 0.0), 28),
            (nextafter(0.29, 1.0), 29),
            (0.285, 28),
            (0.299, 29),
            (0.009, 0),
            (0.0, 0),
        ):
            with self.subTest(seconds=seconds):
                result = simulate(1, seconds, 100.0, 100.0, 0.0)
                self.assertEqual(result.refresh_operations, expected_operations)

    def test_last_complete_tick_can_record_signal_loss(self) -> None:
        # No scan: after 28 ticks the signal is 0.72, after 29 it is 0.71.
        # Keep the threshold away from either floating-point boundary.
        result = simulate(1, 0.29, 100.0, 0.0, 1.0, threshold=0.715)
        self.assertEqual(result.refresh_operations, 0)
        self.assertEqual(result.lost_cells, 1)

    def test_partial_final_tick_does_not_apply_decay(self) -> None:
        result = simulate(1, 0.009, 100.0, 0.0, 100.0)
        self.assertEqual(result.refresh_operations, 0)
        self.assertEqual(result.lost_cells, 0)

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
