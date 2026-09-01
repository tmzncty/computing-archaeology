#!/usr/bin/env python3
"""Conceptual Williams-tube refresh model.

This is a teaching model, not an electrical simulation of a historical CRT.
Cells lose signal over time. A refresh scan restores whichever cells it visits
before their signal falls below a readable threshold.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass
class Cell:
    value: int
    signal: float = 1.0


@dataclass
class Result:
    cells: int
    refreshes_per_second: float
    scan_capacity_per_second: float
    decay_per_second: float
    lost_cells: int
    refresh_operations: int


def simulate(
    cells: int,
    seconds: float,
    refreshes_per_second: float,
    scan_capacity_per_second: float,
    decay_per_second: float,
    threshold: float = 0.25,
) -> Result:
    memory = [Cell(i & 1) for i in range(cells)]
    dt = 1.0 / refreshes_per_second
    cursor = 0
    lost = set()
    refresh_ops = 0
    steps = int(seconds * refreshes_per_second)

    for step in range(steps):
        for index, cell in enumerate(memory):
            cell.signal -= decay_per_second * dt
            if cell.signal < threshold:
                lost.add(index)

        # Derive a cumulative target so fractional per-tick capacity is retained.
        target_refresh_ops = int(
            (step + 1) * scan_capacity_per_second / refreshes_per_second
        )
        visits = target_refresh_ops - refresh_ops
        for _ in range(visits):
            memory[cursor].signal = 1.0
            refresh_ops += 1
            cursor = (cursor + 1) % cells

    return Result(
        cells=cells,
        refreshes_per_second=refreshes_per_second,
        scan_capacity_per_second=scan_capacity_per_second,
        decay_per_second=decay_per_second,
        lost_cells=len(lost),
        refresh_operations=refresh_ops,
    )


def run_scenarios() -> Iterable[Result]:
    # All values below are synthetic teaching parameters.
    for cells in (128, 512, 2048, 4096):
        yield simulate(
            cells=cells,
            seconds=5.0,
            refreshes_per_second=20.0,
            scan_capacity_per_second=8000.0,
            decay_per_second=0.8,
        )


def main() -> None:
    print("Conceptual CRT refresh model")
    print("Synthetic parameters; not Williams-tube performance measurements.\n")
    print(f"{'cells':>7} {'scan/s':>8} {'refresh ops':>12} {'ever lost':>10}")
    for result in run_scenarios():
        print(
            f"{result.cells:7d} "
            f"{result.scan_capacity_per_second:8.0f} "
            f"{result.refresh_operations:12d} "
            f"{result.lost_cells:10d}"
        )

    print("\nTry changing scan_capacity_per_second or decay_per_second.")
    print("The point: capacity competes with the rate at which decaying state can be revisited.")


if __name__ == "__main__":
    main()
