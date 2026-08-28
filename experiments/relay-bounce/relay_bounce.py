#!/usr/bin/env python3
"""Conceptual relay-contact bounce and debouncing demonstration.

The waveform is synthetic and deterministic. It is designed to show how one
intended mechanical closure can create multiple electrical edges, and how
simple qualification policies change the logical interpretation.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Sample:
    time_ms: float
    state: int


DEFAULT_WAVEFORM = [
    Sample(0.00, 0),
    Sample(1.00, 1),
    Sample(1.35, 0),
    Sample(1.70, 1),
    Sample(2.10, 0),
    Sample(2.55, 1),
    Sample(3.10, 0),
    Sample(3.70, 1),
    Sample(10.0, 1),
]


def rising_edges(samples: list[Sample]) -> int:
    count = 0
    previous = samples[0].state
    for sample in samples[1:]:
        if previous == 0 and sample.state == 1:
            count += 1
        previous = sample.state
    return count


def state_at(samples: list[Sample], time_ms: float) -> int:
    state = samples[0].state
    for sample in samples:
        if sample.time_ms > time_ms:
            break
        state = sample.state
    return state


def first_stable_transition(
    samples: list[Sample],
    required_state: int,
    stable_ms: float,
) -> float | None:
    """Return first time the required state begins and remains stable long enough."""
    for index, sample in enumerate(samples):
        if sample.state != required_state:
            continue

        start = sample.time_ms
        end_required = start + stable_ms
        state = required_state
        failed = False

        for later in samples[index + 1 :]:
            if later.time_ms >= end_required:
                break
            state = later.state
            if state != required_state:
                failed = True
                break

        if not failed:
            # If the trace ends before the qualification window, do not claim stability.
            if samples[-1].time_ms >= end_required:
                return start
    return None


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Show how a synthetic bouncing relay closure becomes logical events."
    )
    parser.add_argument(
        "--sample-after",
        type=float,
        default=5.0,
        help="ms after transition start for one-shot settled-state sampling",
    )
    parser.add_argument(
        "--stable-ms",
        type=float,
        default=2.0,
        help="required continuous stable interval for qualification",
    )
    args = parser.parse_args()

    if args.sample_after < 0 or args.stable_ms <= 0:
        parser.error("--sample-after must be >= 0 and --stable-ms must be > 0")

    samples = DEFAULT_WAVEFORM
    print("Synthetic relay contact waveform")
    print("time (ms)  state")
    print("---------  -----")
    for sample in samples:
        print(f"{sample.time_ms:>9.2f}  {sample.state:>5}")

    naive = rising_edges(samples)
    sampled = state_at(samples, args.sample_after)
    stable_start = first_stable_transition(samples, 1, args.stable_ms)

    print()
    print("Three interpretations of one intended closure")
    print(f"naive rising-edge counter:       {naive} events")
    print(
        f"sample once at {args.sample_after:.2f} ms:      state={sampled}"
    )
    if stable_start is None:
        print(
            f"stable-for-{args.stable_ms:.2f}ms qualifier: no accepted closure in trace"
        )
    else:
        accepted_at = stable_start + args.stable_ms
        print(
            f"stable-for-{args.stable_ms:.2f}ms qualifier: accepts one closure at "
            f"~{accepted_at:.2f} ms"
        )

    print()
    print("The waveform and timing thresholds are synthetic teaching values.")
    print("They are not measurements of a specific historical relay.")


if __name__ == "__main__":
    main()
