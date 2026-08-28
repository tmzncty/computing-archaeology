#!/usr/bin/env python3
"""Conceptual latency model for circulating serial memory.

The model represents one access point and N equally spaced word slots moving
past it. Default timing is synthetic; it is not an EDSAC/SEAC emulator.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Access:
    requested: int
    phase_before: int
    slots_waited: int
    wait_ms: float
    phase_after: int


def wait_slots(current_phase: int, requested: int, slots: int) -> int:
    if slots < 2:
        raise ValueError("slots must be at least 2")
    if not (0 <= current_phase < slots and 0 <= requested < slots):
        raise ValueError("phase/request outside serial store")
    return (requested - current_phase) % slots


def access(
    current_phase: int,
    requested: int,
    slots: int,
    slot_ms: float,
) -> Access:
    waited = wait_slots(current_phase, requested, slots)
    # Treat the requested slot as accessible when it reaches the access point.
    # After the word interval passes, the next slot is at the head.
    after = (requested + 1) % slots
    return Access(
        requested=requested,
        phase_before=current_phase,
        slots_waited=waited,
        wait_ms=waited * slot_ms,
        phase_after=after,
    )


def parse_requests(raw: str) -> list[int]:
    try:
        result = [int(part.strip()) for part in raw.split(",") if part.strip()]
    except ValueError as exc:
        raise argparse.ArgumentTypeError("requests must be comma-separated integers") from exc
    if not result:
        raise argparse.ArgumentTypeError("request list cannot be empty")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Expose access latency in a circulating serial memory."
    )
    parser.add_argument("--slots", type=int, default=32)
    parser.add_argument(
        "--slot-ms",
        type=float,
        default=0.05,
        help="synthetic milliseconds per word slot",
    )
    parser.add_argument("--phase", type=int, default=0)
    parser.add_argument(
        "--requests",
        type=parse_requests,
        default=parse_requests("0,1,7,3,31,2"),
    )
    args = parser.parse_args()

    if args.slots < 2:
        parser.error("--slots must be at least 2")
    if args.slot_ms <= 0:
        parser.error("--slot-ms must be positive")
    if not 0 <= args.phase < args.slots:
        parser.error("--phase must be inside the store")
    if any(not 0 <= request < args.slots for request in args.requests):
        parser.error("every request must be inside the store")

    cycle_ms = args.slots * args.slot_ms
    all_waits = [wait_slots(args.phase, address, args.slots) for address in range(args.slots)]

    print("Circulating serial-memory toy model")
    print(f"word slots:              {args.slots}")
    print(f"synthetic slot duration: {args.slot_ms:.4f} ms")
    print(f"full circulation:        {cycle_ms:.4f} ms")
    print(f"initial access phase:    {args.phase}")
    print()
    print("From the initial phase, across every possible address:")
    print(f"  best wait:    {min(all_waits)} slots = {min(all_waits) * args.slot_ms:.4f} ms")
    print(f"  mean wait:    {sum(all_waits) / len(all_waits):.3f} slots = {(sum(all_waits) / len(all_waits)) * args.slot_ms:.4f} ms")
    print(f"  worst wait:   {max(all_waits)} slots = {max(all_waits) * args.slot_ms:.4f} ms")
    print()

    current = args.phase
    total_wait = 0.0
    print("request  phase-in  slots-wait  wait-ms  phase-out")
    print("-------  --------  ----------  -------  ---------")
    for requested in args.requests:
        result = access(current, requested, args.slots, args.slot_ms)
        total_wait += result.wait_ms
        print(
            f"{result.requested:>7}  {result.phase_before:>8}  "
            f"{result.slots_waited:>10}  {result.wait_ms:>7.3f}  "
            f"{result.phase_after:>9}"
        )
        current = result.phase_after

    print()
    print(f"total modeled waiting for request sequence: {total_wait:.4f} ms")
    print("Default timing values are synthetic and demonstrate topology only.")


if __name__ == "__main__":
    main()
