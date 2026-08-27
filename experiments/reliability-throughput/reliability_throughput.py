#!/usr/bin/env python3
"""Availability-throughput tradeoff model for switching technologies.

All default rates and reliability values are hypothetical.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class System:
    name: str
    ops_per_second: float
    mtbf_hours: float
    repair_hours: float

    @property
    def availability(self) -> float:
        if self.mtbf_hours + self.repair_hours == 0:
            return 0.0
        return self.mtbf_hours / (self.mtbf_hours + self.repair_hours)

    @property
    def effective_ops_per_second(self) -> float:
        return self.ops_per_second * self.availability

    @property
    def effective_ops_per_day(self) -> float:
        return self.effective_ops_per_second * 86400.0


def print_system(system: System) -> None:
    print(system.name)
    print(f"  nominal speed:       {system.ops_per_second:,.1f} ops/s")
    print(f"  MTBF assumption:     {system.mtbf_hours:,.2f} h")
    print(f"  repair assumption:   {system.repair_hours:,.2f} h")
    print(f"  availability:        {system.availability:,.2%}")
    print(f"  effective throughput:{system.effective_ops_per_second:,.1f} ops/s")
    print(f"  expected ops/day:    {system.effective_ops_per_day:,.0f}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compare nominal speed with expected throughput after repair downtime."
    )
    parser.add_argument("--a-speed", type=float, default=100.0)
    parser.add_argument("--a-mtbf", type=float, default=100.0)
    parser.add_argument("--a-repair", type=float, default=0.5)
    parser.add_argument("--b-speed", type=float, default=5000.0)
    parser.add_argument("--b-mtbf", type=float, default=8.0)
    parser.add_argument("--b-repair", type=float, default=0.25)
    args = parser.parse_args()

    values = vars(args).values()
    if any(value < 0 for value in values):
        raise SystemExit("all values must be non-negative")
    if args.a_mtbf + args.a_repair <= 0 or args.b_mtbf + args.b_repair <= 0:
        raise SystemExit("MTBF + repair time must be positive for each system")

    a = System("system A", args.a_speed, args.a_mtbf, args.a_repair)
    b = System("system B", args.b_speed, args.b_mtbf, args.b_repair)

    print("Illustrative model only: all default values are hypothetical.")
    print()
    print_system(a)
    print()
    print_system(b)
    print()

    ratio = (
        b.effective_ops_per_second / a.effective_ops_per_second
        if a.effective_ops_per_second
        else float("inf")
    )
    print(f"effective-throughput ratio B/A: {ratio:,.2f}x")
    print(
        "A faster system can produce more work despite lower availability. "
        "Historical reliability still requires measured evidence, not this model."
    )


if __name__ == "__main__":
    main()
