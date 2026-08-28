#!/usr/bin/env python3
"""Estimate wall-clock output time for slow serial printing terminals.

Default Model 33 assumptions:
- 110 baud
- 11 signal units per character frame
- therefore about 10 characters per second

This is a bandwidth model, not an electromechanical Teletype emulator.
"""

from __future__ import annotations

import argparse
import time


DEFAULT_EXAMPLES = [
    ("short prompt", 12),
    ("72-column line", 72),
    ("compact error", 24),
    ("500-char help", 500),
    ("1000-char listing", 1000),
    ("80x24 screenful", 80 * 24),
]


def chars_per_second(baud: float, frame_bits: float) -> float:
    if baud <= 0 or frame_bits <= 0:
        raise ValueError("baud and frame bits must be positive")
    return baud / frame_bits


def transmit_seconds(characters: int, baud: float, frame_bits: float) -> float:
    if characters < 0:
        raise ValueError("characters cannot be negative")
    return characters / chars_per_second(baud, frame_bits)


def format_duration(seconds: float) -> str:
    if seconds < 60:
        return f"{seconds:.2f} s"
    minutes, remainder = divmod(seconds, 60)
    if minutes < 60:
        return f"{int(minutes)}m {remainder:04.1f}s"
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}h {int(minutes)}m {remainder:04.1f}s"


def print_examples(baud: float, frame_bits: float) -> None:
    cps = chars_per_second(baud, frame_bits)
    print(f"baud={baud:g}, frame={frame_bits:g} signal units/character")
    print(f"effective rate: {cps:.3f} characters/second")
    print()
    print("scenario             chars    output time")
    print("-------------------  -------  ----------------")
    for label, count in DEFAULT_EXAMPLES:
        seconds = transmit_seconds(count, baud, frame_bits)
        print(f"{label:<19}  {count:>7}  {format_duration(seconds):>16}")


def live_print(text: str, baud: float, frame_bits: float) -> None:
    delay = 1.0 / chars_per_second(baud, frame_bits)
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Turn serial-terminal bandwidth into a user-visible time budget."
    )
    parser.add_argument("--baud", type=float, default=110.0)
    parser.add_argument("--frame-bits", type=float, default=11.0)
    parser.add_argument("--characters", type=int)
    parser.add_argument("--text")
    parser.add_argument(
        "--live",
        action="store_true",
        help="print --text at the modeled character rate (intentionally slow)",
    )
    args = parser.parse_args()

    if args.baud <= 0:
        parser.error("--baud must be positive")
    if args.frame_bits <= 0:
        parser.error("--frame-bits must be positive")
    if args.characters is not None and args.characters < 0:
        parser.error("--characters cannot be negative")
    if args.live and args.text is None:
        parser.error("--live requires --text")

    print_examples(args.baud, args.frame_bits)

    if args.characters is not None:
        seconds = transmit_seconds(args.characters, args.baud, args.frame_bits)
        print()
        print(
            f"{args.characters:,} characters -> {format_duration(seconds)} "
            f"at {args.baud:g} baud"
        )

    if args.text is not None:
        seconds = transmit_seconds(len(args.text), args.baud, args.frame_bits)
        print()
        print(
            f"text length {len(args.text)} -> {format_duration(seconds)} "
            f"at {args.baud:g} baud"
        )
        if args.live:
            print("Live modeled output:")
            live_print(args.text, args.baud, args.frame_bits)


if __name__ == "__main__":
    main()
