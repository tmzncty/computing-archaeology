#!/usr/bin/env python3
"""Tiny rotational-memory timing model.

This is a teaching model for the geometry of a drum-resident instruction
sequence. It is not an IBM 650 emulator and does not reproduce SOAP.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class RunResult:
    execution_slots: int
    wait_slots: int

    @property
    def total_slots(self) -> int:
        return self.execution_slots + self.wait_slots

    @property
    def utilization(self) -> float:
        if self.total_slots == 0:
            return 0.0
        return self.execution_slots / self.total_slots


def parse_latencies(text: str) -> list[int]:
    values = [int(part.strip()) for part in text.split(",") if part.strip()]
    if not values:
        raise argparse.ArgumentTypeError("provide at least one latency")
    if any(value < 1 for value in values):
        raise argparse.ArgumentTypeError("latencies must be positive integers")
    return values


def naive_placement(count: int, slots: int) -> list[int]:
    if count > slots:
        raise ValueError("this simple model requires instruction count <= drum slots")
    return list(range(count))


def greedy_placement(latencies: list[int], slots: int) -> list[int]:
    """Place each next instruction near when the previous one finishes.

    A simple first-fit policy is used if the ideal slot is already occupied.
    """
    if len(latencies) > slots:
        raise ValueError("this simple model requires instruction count <= drum slots")

    placement = [0]
    occupied = {0}

    for latency in latencies[:-1]:
        ideal = (placement[-1] + latency) % slots
        chosen = None
        for offset in range(slots):
            candidate = (ideal + offset) % slots
            if candidate not in occupied:
                chosen = candidate
                break
        assert chosen is not None
        placement.append(chosen)
        occupied.add(chosen)

    return placement


def run_loop(
    latencies: list[int],
    placement: list[int],
    slots: int,
    loops: int,
) -> RunResult:
    if len(latencies) != len(placement):
        raise ValueError("latency and placement lists must have equal length")

    position = placement[0]
    execution = 0
    waiting = 0

    for _ in range(loops):
        for index, latency in enumerate(latencies):
            execution += latency
            position = (position + latency) % slots

            next_index = (index + 1) % len(latencies)
            target = placement[next_index]
            wait = (target - position) % slots
            waiting += wait
            position = target

    return RunResult(execution, waiting)


def slot_microseconds(rpm: float, slots: int) -> float:
    return 60_000_000.0 / (rpm * slots)


def format_result(label: str, result: RunResult, us_per_slot: float) -> str:
    return (
        f"{label}\n"
        f"  execution: {result.execution_slots:>8} slots "
        f"({result.execution_slots * us_per_slot / 1000:,.3f} ms)\n"
        f"  waiting:   {result.wait_slots:>8} slots "
        f"({result.wait_slots * us_per_slot / 1000:,.3f} ms)\n"
        f"  total:     {result.total_slots:>8} slots "
        f"({result.total_slots * us_per_slot / 1000:,.3f} ms)\n"
        f"  useful-time fraction: {result.utilization:>7.2%}"
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compare consecutive and timing-aware placement on a rotating drum."
    )
    parser.add_argument(
        "--latencies",
        type=parse_latencies,
        default=parse_latencies("3,8,2,5,4,7"),
        help="comma-separated instruction execution times in drum slots",
    )
    parser.add_argument("--slots", type=int, default=50, help="angular slots per revolution")
    parser.add_argument("--rpm", type=float, default=12_500.0, help="drum speed")
    parser.add_argument("--loops", type=int, default=10, help="loop repetitions")
    return parser


def main() -> None:
    args = build_parser().parse_args()

    if args.slots < 1:
        raise SystemExit("--slots must be positive")
    if args.rpm <= 0:
        raise SystemExit("--rpm must be positive")
    if args.loops < 1:
        raise SystemExit("--loops must be positive")

    latencies = args.latencies
    naive = naive_placement(len(latencies), args.slots)
    greedy = greedy_placement(latencies, args.slots)
    us_per_slot = slot_microseconds(args.rpm, args.slots)

    naive_result = run_loop(latencies, naive, args.slots, args.loops)
    greedy_result = run_loop(latencies, greedy, args.slots, args.loops)

    print(f"drum: {args.rpm:g} rpm, {args.slots} slots/revolution")
    print(f"time per slot: {us_per_slot:.3f} us")
    print(f"instruction latencies: {latencies}")
    print(f"consecutive placement: {naive}")
    print(f"timing-aware placement: {greedy}")
    print()
    print(format_result("consecutive", naive_result, us_per_slot))
    print()
    print(format_result("timing-aware", greedy_result, us_per_slot))

    saved = naive_result.total_slots - greedy_result.total_slots
    print()
    print(
        f"saved by placement in this model: {saved} slots "
        f"({saved * us_per_slot / 1000:,.3f} ms)"
    )


if __name__ == "__main__":
    main()
