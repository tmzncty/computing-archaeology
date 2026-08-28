#!/usr/bin/env python3
"""Conceptual staged bootstrap model."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Stage:
    name: str
    manual_words: int
    can_load_words: int
    source: str


def main() -> None:
    stages = [
        Stage("front-panel seed", 17, 128, "toggle switches"),
        Stage("simple tape loader", 0, 2048, "paper tape"),
        Stage("system loader", 0, 32768, "richer medium/format"),
        Stage("operating environment", 0, 1_000_000, "filesystem/devices"),
    ]

    print("Conceptual bootstrap chain")
    print("Teaching capacities; only the staged-loading idea is historical.\n")
    print(f"{'stage':<24} {'manual words':>12} {'can load':>12}  source")
    for stage in stages:
        print(f"{stage.name:<24} {stage.manual_words:12d} {stage.can_load_words:12d}  {stage.source}")

    manual = sum(stage.manual_words for stage in stages)
    final_capacity = stages[-1].can_load_words
    print(f"\nManual entry: {manual} words")
    print(f"Final conceptual load capability: {final_capacity:,} words")
    print(f"Capability/manual ratio: {final_capacity / manual:,.0f}:1")
    print("\nA tiny manually created capability can load a much larger one.")


if __name__ == "__main__":
    main()
