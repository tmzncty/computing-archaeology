#!/usr/bin/env python3
"""Illustrative machine-utilization model for direct vs batch operation.

The defaults are hypothetical. This is not a reconstruction of a specific
IBM 704 installation.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Strategy:
    useful_seconds: float
    occupied_seconds: float

    @property
    def utilization(self) -> float:
        return 0.0 if self.occupied_seconds == 0 else self.useful_seconds / self.occupied_seconds


def direct_strategy(jobs: int, compute: float, setup: float) -> Strategy:
    useful = jobs * compute
    occupied = jobs * (setup + compute)
    return Strategy(useful, occupied)


def batch_strategy(
    jobs: int,
    compute: float,
    batch_setup: float,
    transition: float,
) -> Strategy:
    useful = jobs * compute
    occupied = batch_setup + jobs * compute + max(0, jobs - 1) * transition
    return Strategy(useful, occupied)


def format_strategy(name: str, strategy: Strategy, jobs: int) -> str:
    elapsed_h = strategy.occupied_seconds / 3600.0
    jobs_per_hour = jobs / elapsed_h if elapsed_h else 0.0
    return (
        f"{name}\n"
        f"  useful compute:     {strategy.useful_seconds:8.1f} s\n"
        f"  machine occupancy:  {strategy.occupied_seconds:8.1f} s\n"
        f"  compute utilization:{strategy.utilization:8.2%}\n"
        f"  throughput:         {jobs_per_hour:8.2f} jobs/hour"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compare machine occupancy under direct per-job setup and batching."
    )
    parser.add_argument("--jobs", type=int, default=20)
    parser.add_argument("--compute", type=float, default=30.0, help="useful seconds per job")
    parser.add_argument(
        "--direct-setup",
        type=float,
        default=120.0,
        help="machine-occupied setup seconds before every direct job",
    )
    parser.add_argument(
        "--batch-setup",
        type=float,
        default=240.0,
        help="machine-occupied setup seconds paid once per batch",
    )
    parser.add_argument(
        "--transition",
        type=float,
        default=3.0,
        help="automated/standardized transition seconds between batch jobs",
    )
    args = parser.parse_args()

    if args.jobs < 1:
        raise SystemExit("--jobs must be positive")
    if min(args.compute, args.direct_setup, args.batch_setup, args.transition) < 0:
        raise SystemExit("time arguments must be non-negative")

    direct = direct_strategy(args.jobs, args.compute, args.direct_setup)
    batch = batch_strategy(args.jobs, args.compute, args.batch_setup, args.transition)

    print("Illustrative model only: default times are hypothetical.")
    print(f"jobs: {args.jobs}, useful compute/job: {args.compute:g} s")
    print()
    print(format_strategy("direct console-style operation", direct, args.jobs))
    print()
    print(format_strategy("batch operation", batch, args.jobs))
    print()

    improvement = direct.occupied_seconds / batch.occupied_seconds if batch.occupied_seconds else float("inf")
    print(f"same {args.jobs} jobs complete {improvement:.2f}x sooner in the batch model")
    print(
        "This says nothing about individual response time: batching may improve "
        "throughput while making a programmer wait longer for a particular result."
    )


if __name__ == "__main__":
    main()
