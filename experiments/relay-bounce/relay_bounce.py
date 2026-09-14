#!/usr/bin/env python3
"""Conceptual relay-contact bounce and debouncing demonstration.

The waveform is synthetic and deterministic. It is designed to show how one
intended mechanical closure can create multiple electrical edges, and how
simple qualification policies change the logical interpretation.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Sample:
    time_ms: float
    state: int


@dataclass(frozen=True)
class DebounceEvent:
    time_ms: Fraction
    kind: str
    raw_state: int
    qualified_state: int
    candidate_state: int | None
    deadline_ms: Fraction | None


@dataclass(frozen=True)
class DebounceTrace:
    events: tuple[DebounceEvent, ...]
    raw_closures: int
    qualified_closures: int
    final_state: int
    horizon_ms: Fraction


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


def _exact_ms(value: float, label: str) -> Fraction:
    """Interpret a finite int/float's decimal spelling without binary epsilon."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} must be a finite number")
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError(f"{label} must be a finite number")
    return Fraction(str(value))


def trace_debounce(samples: list[Sample], stable_ms: float) -> DebounceTrace:
    """Trace a synthetic continuous qualifier, initially open (0).

    Both states need the same stable interval. Times use Fraction(str(value)):
    their decimal spellings, not binary-float approximations, define deadlines.
    A deadline is processed before an input edge at the same time. The last
    sample bounds observation; a pending later deadline is never accepted.

    Event raw/qualified fields describe those states at the event. Candidate
    fields identify the involved candidate: cancellation and qualification
    events retain it before clearing it. A deadline event precedes the matching
    qualified-change event, whose qualified_state is the new state.
    """
    interval = _exact_ms(stable_ms, "stable_ms")
    if interval <= 0:
        raise ValueError("stable_ms must be > 0")
    try:
        observations = tuple(samples)
    except TypeError as exc:
        raise ValueError("samples must be a nonempty sequence of Sample values") from exc
    if not observations:
        raise ValueError("samples must not be empty")

    timeline: list[tuple[Fraction, int]] = []
    for index, sample in enumerate(observations):
        if not isinstance(sample, Sample):
            raise ValueError(f"samples[{index}] must be a Sample")
        time_ms = _exact_ms(sample.time_ms, f"samples[{index}].time_ms")
        if time_ms < 0 or (timeline and time_ms <= timeline[-1][0]):
            raise ValueError("sample times must be nonnegative and strictly increasing")
        if isinstance(sample.state, bool) or not isinstance(sample.state, int) or sample.state not in (0, 1):
            raise ValueError(f"samples[{index}].state must be integer 0 or 1")
        timeline.append((time_ms, sample.state))

    events: list[DebounceEvent] = []
    raw_state = timeline[0][1]
    qualified_state = 0
    candidate_state: int | None = None
    deadline_ms: Fraction | None = None
    raw_closures = 0
    qualified_closures = 0

    def emit(time_ms: Fraction, kind: str) -> None:
        events.append(DebounceEvent(
            time_ms, kind, raw_state, qualified_state, candidate_state, deadline_ms,
        ))

    def start_candidate(time_ms: Fraction) -> None:
        nonlocal candidate_state, deadline_ms
        candidate_state = raw_state
        deadline_ms = time_ms + interval
        emit(time_ms, "candidate-start")

    def qualify_due(time_ms: Fraction) -> None:
        nonlocal candidate_state, deadline_ms, qualified_state, qualified_closures
        if candidate_state is not None and deadline_ms is not None and deadline_ms <= time_ms:
            emit(deadline_ms, "deadline")
            qualified_state = candidate_state
            if qualified_state == 1:
                qualified_closures += 1
            emit(deadline_ms, "qualified-change")
            candidate_state = None
            deadline_ms = None

    emit(timeline[0][0], "initial")
    if raw_state != qualified_state:
        start_candidate(timeline[0][0])

    for time_ms, state in timeline[1:]:
        # The old raw state persists up to this observation, including a
        # qualification deadline exactly equal to this input edge's time.
        qualify_due(time_ms)
        if state == raw_state:
            continue
        if raw_state == 0 and state == 1:
            raw_closures += 1
        raw_state = state
        emit(time_ms, "raw-change")
        if candidate_state is not None:
            emit(time_ms, "candidate-cancel")
            candidate_state = None
            deadline_ms = None
        if raw_state != qualified_state:
            start_candidate(time_ms)

    horizon_ms = timeline[-1][0]
    emit(horizon_ms, "horizon")
    return DebounceTrace(
        tuple(events), raw_closures, qualified_closures, qualified_state, horizon_ms,
    )


def _format_ms(value: Fraction) -> str:
    """Render our terminating decimal times exactly, with at least two places."""
    denominator = value.denominator
    twos = fives = 0
    while denominator % 2 == 0:
        denominator //= 2
        twos += 1
    while denominator % 5 == 0:
        denominator //= 5
        fives += 1
    # Inputs are finite decimal spellings; addition preserves this property.
    assert denominator == 1
    places = max(2, twos, fives)
    scale = 10 ** places
    scaled = value.numerator * scale // value.denominator
    whole, fraction = divmod(scaled, scale)
    return f"{whole}.{fraction:0{places}d}"


def print_trace(trace: DebounceTrace) -> None:
    print()
    print("Continuous qualified-state trace (initial output=0; deadline before input edge)")
    print("time (ms)  event             raw  qualified  candidate  deadline (ms)")
    for event in trace.events:
        candidate = "-" if event.candidate_state is None else str(event.candidate_state)
        deadline = "-" if event.deadline_ms is None else _format_ms(event.deadline_ms)
        print(
            f"{_format_ms(event.time_ms):>9}  {event.kind:<16}  {event.raw_state:>3}  "
            f"{event.qualified_state:>9}  {candidate:>9}  {deadline:>13}"
        )
    print(f"raw rising edges: {trace.raw_closures}")
    print(f"qualified rising edges: {trace.qualified_closures}")
    print(f"final qualified state at {_format_ms(trace.horizon_ms)} ms: {trace.final_state}")
    print("The three-way comparison above reports only the first accepted closure.")
    print("This continuous qualifier is a synthetic policy, not a historical relay circuit.")


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
    parser.add_argument(
        "--trace",
        action="store_true",
        help="also trace continuous opening/closing qualification and event counts",
    )
    args = parser.parse_args()

    if not math.isfinite(args.sample_after) or not math.isfinite(args.stable_ms):
        parser.error("--sample-after and --stable-ms must be finite")
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
    if args.trace:
        print_trace(trace_debounce(samples, args.stable_ms))


if __name__ == "__main__":
    main()
