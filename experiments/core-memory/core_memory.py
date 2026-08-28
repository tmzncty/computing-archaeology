#!/usr/bin/env python3
"""Small conceptual model of coincident-current magnetic core memory.

This program exposes selection geometry and destructive read/restore behavior.
It does not numerically simulate ferrite hysteresis, currents, timing, or noise.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass
class ReadResult:
    row: int
    col: int
    observed_bit: int
    sense_pulse: bool
    restored: bool


class CorePlane:
    def __init__(self, size: int = 4) -> None:
        if size < 2:
            raise ValueError("size must be at least 2")
        self.size = size
        self.bits = [[0 for _ in range(size)] for _ in range(size)]

    def _check(self, row: int, col: int) -> None:
        if not (0 <= row < self.size and 0 <= col < self.size):
            raise IndexError("row/col outside plane")

    def seed_checkerboard(self) -> None:
        for row in range(self.size):
            for col in range(self.size):
                self.bits[row][col] = (row + col) % 2

    def write(self, row: int, col: int, value: int) -> None:
        self._check(row, col)
        if value not in (0, 1):
            raise ValueError("core value must be 0 or 1")
        self.bits[row][col] = value

    def selection_map(self, row: int, col: int) -> list[list[float]]:
        """Return normalized excitation: 1.0 target, 0.5 half-selected, 0 elsewhere."""
        self._check(row, col)
        result: list[list[float]] = []
        for r in range(self.size):
            line: list[float] = []
            for c in range(self.size):
                excitation = 0.0
                if r == row:
                    excitation += 0.5
                if c == col:
                    excitation += 0.5
                line.append(excitation)
            result.append(line)
        return result

    def destructive_read(self, row: int, col: int, restore: bool = True) -> ReadResult:
        """Force selected bit to 0 and infer prior value from whether it changed."""
        self._check(row, col)
        old = self.bits[row][col]
        sense_pulse = old == 1

        # Conceptual read: forcing the target toward zero destroys a stored one.
        self.bits[row][col] = 0

        restored = False
        if restore and old == 1:
            self.bits[row][col] = 1
            restored = True

        return ReadResult(
            row=row,
            col=col,
            observed_bit=old,
            sense_pulse=sense_pulse,
            restored=restored,
        )

    def render(self) -> str:
        return "\n".join(" ".join(str(bit) for bit in row) for row in self.bits)


def render_selection(selection: list[list[float]]) -> str:
    return "\n".join(" ".join(f"{value:.1f}" for value in row) for row in selection)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Demonstrate coincident selection and destructive core-memory reads."
    )
    parser.add_argument("--size", type=int, default=4)
    parser.add_argument("--row", type=int, default=1)
    parser.add_argument("--col", type=int, default=2)
    parser.add_argument(
        "--no-restore",
        action="store_true",
        help="leave a destructive read cleared instead of restoring a stored 1",
    )
    args = parser.parse_args()

    plane = CorePlane(args.size)
    plane.seed_checkerboard()
    plane._check(args.row, args.col)

    print("Initial conceptual core plane")
    print(plane.render())
    print()

    print(f"Normalized selection for row={args.row}, col={args.col}")
    print("0.5 = half-selected; 1.0 = selected intersection")
    print(render_selection(plane.selection_map(args.row, args.col)))
    print()

    before = plane.bits[args.row][args.col]
    result = plane.destructive_read(args.row, args.col, restore=not args.no_restore)

    print(f"Bit before read: {before}")
    print(f"Sense pulse observed: {result.sense_pulse}")
    print(f"Recovered logical value: {result.observed_bit}")
    print(f"Restored after read: {result.restored}")
    print()

    print("Plane after read sequence")
    print(plane.render())

    if args.no_restore and before == 1:
        print()
        print("The selected 1 is now lost: destructive read was left unrestored.")


if __name__ == "__main__":
    main()
