#!/usr/bin/env python3
"""Explore carry propagation across positional radices.

This is a teaching model, not a simulator of any historical calculator.
It counts abstract digit updates and carry-boundary crossings while repeatedly
incrementing a counter.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class RadixResult:
    radix: int
    digits_for_range: int
    increments: int
    digit_updates: int
    boundary_carries: int
    max_chain: int

    @property
    def avg_digit_updates(self) -> float:
        return self.digit_updates / self.increments if self.increments else 0.0

    @property
    def avg_boundary_carries(self) -> float:
        return self.boundary_carries / self.increments if self.increments else 0.0


def digits_required(max_value: int, radix: int) -> int:
    if max_value < 0:
        raise ValueError("max_value must be non-negative")
    if radix < 2:
        raise ValueError("radix must be at least 2")
    if max_value == 0:
        return 1
    return math.ceil(math.log(max_value + 1, radix))


def carry_chain_for_increment(value: int, radix: int) -> int:
    """Return the number of digit boundaries crossed by value -> value + 1."""
    chain = 0
    while value % radix == radix - 1:
        chain += 1
        value //= radix
    return chain


def simulate(radix: int, max_value: int, increments: int) -> RadixResult:
    if increments <= 0:
        raise ValueError("increments must be positive")

    digits = digits_required(max_value, radix)
    period = radix**digits
    if period <= 1:
        period = radix

    digit_updates = 0
    boundary_carries = 0
    max_chain = 0

    value = 0
    for _ in range(increments):
        chain = carry_chain_for_increment(value, radix)
        boundary_carries += chain
        digit_updates += 1 + chain
        max_chain = max(max_chain, chain)
        value = (value + 1) % period

    return RadixResult(
        radix=radix,
        digits_for_range=digits,
        increments=increments,
        digit_updates=digit_updates,
        boundary_carries=boundary_carries,
        max_chain=max_chain,
    )


def synthetic_cost(
    result: RadixResult,
    wheel_cost: float,
    state_cost: float,
    carry_cost: float,
) -> float:
    """A deliberately synthetic cost model.

    wheel_cost: fixed cost per digit position.
    state_cost: cost per stable state per digit position.
    carry_cost: dynamic cost per observed boundary carry.

    These weights are not measurements of historical machines.
    """
    fixed = result.digits_for_range * wheel_cost
    state_complexity = result.digits_for_range * result.radix * state_cost
    dynamic = result.boundary_carries * carry_cost / result.increments
    return fixed + state_complexity + dynamic


def parse_radices(raw: str) -> list[int]:
    values = [int(part.strip()) for part in raw.split(",") if part.strip()]
    if not values or any(value < 2 for value in values):
        raise argparse.ArgumentTypeError("radices must be comma-separated integers >= 2")
    return values


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compare positional radices under a simple carry-propagation model."
    )
    parser.add_argument("--max-value", type=int, default=999_999)
    parser.add_argument("--increments", type=int, default=100_000)
    parser.add_argument("--radices", type=parse_radices, default=parse_radices("2,4,8,10,16"))
    parser.add_argument("--wheel-cost", type=float, default=10.0)
    parser.add_argument("--state-cost", type=float, default=0.5)
    parser.add_argument("--carry-cost", type=float, default=5.0)
    args = parser.parse_args()

    if args.max_value < 1:
        parser.error("--max-value must be at least 1")
    if args.increments < 1:
        parser.error("--increments must be at least 1")

    print("Carry propagation under repeated +1")
    print(f"target numeric range: 0..{args.max_value:,}")
    print(f"simulated increments: {args.increments:,}")
    print()
    print(
        "radix  digits  avg updates  avg carries  max chain  synthetic cost"
    )
    print("-----  ------  -----------  -----------  ---------  --------------")

    for radix in args.radices:
        result = simulate(radix, args.max_value, args.increments)
        cost = synthetic_cost(
            result,
            wheel_cost=args.wheel_cost,
            state_cost=args.state_cost,
            carry_cost=args.carry_cost,
        )
        print(
            f"{result.radix:>5}  "
            f"{result.digits_for_range:>6}  "
            f"{result.avg_digit_updates:>11.5f}  "
            f"{result.avg_boundary_carries:>11.5f}  "
            f"{result.max_chain:>9}  "
            f"{cost:>14.3f}"
        )

    print()
    print("Synthetic-cost weights (not historical measurements):")
    print(f"  wheel cost per digit position = {args.wheel_cost}")
    print(f"  state cost per radix state    = {args.state_cost}")
    print(f"  carry cost per avg boundary   = {args.carry_cost}")
    print()
    print("Change the weights and watch the apparent 'best' radix move.")


if __name__ == "__main__":
    main()
