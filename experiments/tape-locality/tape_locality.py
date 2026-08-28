#!/usr/bin/env python3
"""Synthetic sequential-tape locality and blocking model."""

from __future__ import annotations

import random
from dataclasses import dataclass


@dataclass
class AccessResult:
    requests: int
    movement: int


def movement_cost(order: list[int]) -> AccessResult:
    position = 0
    movement = 0
    for target in order:
        movement += abs(target - position)
        position = target
    return AccessResult(len(order), movement)


def media_efficiency(record_bytes: int, records_per_block: int, gap_bytes_equiv: int) -> float:
    useful = record_bytes * records_per_block
    physical = useful + gap_bytes_equiv
    return useful / physical


def main() -> None:
    records = list(range(1000))
    sequential = records[:]
    random_order = records[:]
    random.Random(1952).shuffle(random_order)

    seq = movement_cost(sequential)
    rnd = movement_cost(random_order)

    print("Synthetic tape-position model")
    print(f"sequential movement units: {seq.movement}")
    print(f"random movement units:     {rnd.movement}")
    print(f"random/sequential ratio:   {rnd.movement / max(seq.movement, 1):.1f}x")

    print("\nSynthetic interblock-gap efficiency")
    print(f"{'records/block':>13} {'efficiency':>12}")
    for block in (1, 2, 5, 10, 20, 50, 100):
        efficiency = media_efficiency(record_bytes=100, records_per_block=block, gap_bytes_equiv=200)
        print(f"{block:13d} {efficiency:11.1%}")

    print("\nAll distances/gap equivalents are teaching parameters, not historical measurements.")


if __name__ == "__main__":
    main()
