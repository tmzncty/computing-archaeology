#!/usr/bin/env python3
"""Compare direct polynomial evaluation with finite-difference generation.

This is an explanatory cost model, not a simulation of Babbage's machinery.
"""

from __future__ import annotations

from dataclasses import dataclass


COST_ADD = 1
COST_MUL = 10


@dataclass
class Counts:
    additions: int = 0
    multiplications: int = 0

    def weighted_cost(self) -> int:
        return self.additions * COST_ADD + self.multiplications * COST_MUL

    def __iadd__(self, other: "Counts") -> "Counts":
        self.additions += other.additions
        self.multiplications += other.multiplications
        return self


def horner(coefficients: list[int], x: int) -> tuple[int, Counts]:
    """Evaluate coefficients[0] * x^d + ... + coefficients[-1]."""
    if not coefficients:
        raise ValueError("polynomial must have at least one coefficient")

    value = coefficients[0]
    counts = Counts()
    for coefficient in coefficients[1:]:
        value *= x
        counts.multiplications += 1
        value += coefficient
        counts.additions += 1
    return value, counts


def build_difference_state(coefficients: list[int]) -> tuple[list[int], Counts]:
    """Build [f(0), Δf(0), Δ²f(0), ...] for a polynomial."""
    degree = len(coefficients) - 1
    values: list[int] = []
    counts = Counts()

    for x in range(degree + 1):
        value, direct_counts = horner(coefficients, x)
        values.append(value)
        counts += direct_counts

    state = [values[0]]
    row = values
    while len(row) > 1:
        next_row = []
        for left, right in zip(row, row[1:]):
            next_row.append(right - left)
            counts.additions += 1  # subtraction is treated as signed addition here
        row = next_row
        state.append(row[0])

    return state, counts


def advance_difference_state(state: list[int], counts: Counts) -> None:
    """Advance from n to n+1 using additions only."""
    # For forward differences:
    # f(n+1)   = f(n)   + Δf(n)
    # Δf(n+1)  = Δf(n)  + Δ²f(n)
    # ...
    # Updating from low order upward preserves the old higher difference
    # until it is consumed.
    for order in range(len(state) - 1):
        state[order] += state[order + 1]
        counts.additions += 1


def direct_series(coefficients: list[int], count: int) -> tuple[list[int], Counts]:
    values = []
    counts = Counts()
    for x in range(count):
        value, local_counts = horner(coefficients, x)
        values.append(value)
        counts += local_counts
    return values, counts


def difference_series(coefficients: list[int], count: int) -> tuple[list[int], Counts]:
    if count <= 0:
        return [], Counts()

    state, counts = build_difference_state(coefficients)
    values = [state[0]]
    for _ in range(1, count):
        advance_difference_state(state, counts)
        values.append(state[0])
    return values, counts


def describe(label: str, values: list[int], counts: Counts) -> None:
    print(label)
    print(f"  values:          {values}")
    print(f"  additions:       {counts.additions}")
    print(f"  multiplications: {counts.multiplications}")
    print(f"  weighted cost:   {counts.weighted_cost()}")


def main() -> None:
    # f(x) = 3x^3 - 2x^2 + 5x + 7
    coefficients = [3, -2, 5, 7]
    count = 16

    direct_values, direct_counts = direct_series(coefficients, count)
    difference_values, difference_counts = difference_series(coefficients, count)

    if direct_values != difference_values:
        raise AssertionError("finite-difference generation disagrees with direct evaluation")

    print("Polynomial: 3x^3 - 2x^2 + 5x + 7")
    print(f"Samples:    x = 0..{count - 1}")
    print(f"Cost model: add={COST_ADD}, multiply={COST_MUL}\n")

    describe("Direct Horner evaluation", direct_values, direct_counts)
    print()
    describe("Finite-difference generation", difference_values, difference_counts)

    print("\nNote: finite differences pay an initialization cost, then advance using additions only.")
    print("Change the sample count and cost ratio to see when that tradeoff becomes attractive.")


if __name__ == "__main__":
    main()
