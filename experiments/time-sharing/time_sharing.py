#!/usr/bin/env python3
"""Toy model for fixed interactive request intervals and shared CPU demand.

The model does not reproduce CTSS scheduling. It illustrates why request streams
separated by long pauses and requiring short CPU bursts can share one processor
while users still perceive relatively quick service at modest load.
"""

from __future__ import annotations

import argparse
import heapq
import math
from dataclasses import dataclass


@dataclass(order=True)
class Request:
    arrival: float
    user: int
    sequence: int
    cpu: float


@dataclass
class Metrics:
    completed: int
    mean_response: float
    max_response: float
    cpu_utilization: float
    makespan: float


def _require_positive_finite(name: str, value: float) -> None:
    """Reject values that cannot advance this discrete-event simulation."""
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be a positive finite number")


def per_user_offered_load(cpu_burst: float, request_interval: float) -> float:
    """Return one request stream's demand per fixed request-start interval."""
    _require_positive_finite("cpu_burst", cpu_burst)
    _require_positive_finite("request_interval", request_interval)
    return cpu_burst / request_interval


def offered_load(users: int, cpu_burst: float, request_interval: float) -> float:
    """Return aggregate demand for the arrivals produced by build_requests()."""
    return users * per_user_offered_load(cpu_burst, request_interval)


def build_requests(
    users: int, rounds: int, request_interval: float, cpu_burst: float
) -> list[Request]:
    """Create deterministic staggered interactive requests.

    Each user emits a request once per fixed request-start interval. Initial
    arrivals are staggered evenly so all users do not synchronize at t=0. CPU
    service and queueing do not move later arrivals.
    """
    _require_positive_finite("request_interval", request_interval)
    _require_positive_finite("cpu_burst", cpu_burst)

    requests: list[Request] = []
    spacing = request_interval / users if users else 0.0
    for user in range(users):
        first = user * spacing
        for sequence in range(rounds):
            requests.append(
                Request(
                    arrival=first + sequence * request_interval,
                    user=user,
                    sequence=sequence,
                    cpu=cpu_burst,
                )
            )
    requests.sort()
    return requests


def simulate_round_robin(requests: list[Request], quantum: float) -> Metrics:
    _require_positive_finite("quantum", quantum)
    for request in requests:
        if not math.isfinite(request.arrival) or request.arrival < 0:
            raise ValueError("request arrival must be a non-negative finite number")
        _require_positive_finite("request cpu", request.cpu)
    if not requests:
        return Metrics(0, 0.0, 0.0, 0.0, 0.0)

    pending = list(requests)
    ready: list[tuple[int, int, float, float]] = []
    index = 0
    now = 0.0
    busy = 0.0
    completion_response: list[float] = []
    tie = 0

    while index < len(pending) or ready:
        if not ready and index < len(pending) and now < pending[index].arrival:
            now = pending[index].arrival

        while index < len(pending) and pending[index].arrival <= now + 1e-12:
            req = pending[index]
            heapq.heappush(ready, (tie, req.user, req.cpu, req.arrival))
            tie += 1
            index += 1

        if not ready:
            continue

        order, user, remaining, arrival = heapq.heappop(ready)
        run = min(quantum, remaining)
        now += run
        busy += run
        remaining -= run

        while index < len(pending) and pending[index].arrival <= now + 1e-12:
            req = pending[index]
            heapq.heappush(ready, (tie, req.user, req.cpu, req.arrival))
            tie += 1
            index += 1

        if remaining <= 1e-12:
            completion_response.append(now - arrival)
        else:
            heapq.heappush(ready, (tie, user, remaining, arrival))
            tie += 1

    makespan = now
    return Metrics(
        completed=len(completion_response),
        mean_response=sum(completion_response) / len(completion_response),
        max_response=max(completion_response),
        cpu_utilization=busy / makespan if makespan else 0.0,
        makespan=makespan,
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Explore fixed request arrivals, shared CPU load, and response time."
    )
    parser.add_argument("--users", type=int, default=20)
    parser.add_argument("--rounds", type=int, default=20)
    parser.add_argument(
        "--think",
        dest="request_interval",
        metavar="SECONDS",
        type=float,
        default=10.0,
        help="fixed seconds between request starts (open-loop)",
    )
    parser.add_argument(
        "--cpu", type=float, default=0.05, help="CPU seconds per request"
    )
    parser.add_argument(
        "--quantum", type=float, default=0.02, help="round-robin quantum seconds"
    )
    args = parser.parse_args()

    if args.users < 1 or args.rounds < 1:
        parser.error("--users and --rounds must be positive")
    if any(
        not math.isfinite(value) or value <= 0
        for value in (args.request_interval, args.cpu, args.quantum)
    ):
        parser.error("--think, --cpu, and --quantum must be positive finite numbers")

    single = per_user_offered_load(args.cpu, args.request_interval)
    load = offered_load(args.users, args.cpu, args.request_interval)
    requests = build_requests(args.users, args.rounds, args.request_interval, args.cpu)
    metrics = simulate_round_robin(requests, args.quantum)

    print("Interactive sharing toy model")
    print(f"users:                 {args.users}")
    print(f"requests/user:         {args.rounds}")
    print(f"request-start interval: {args.request_interval:.3f} s")
    print(f"CPU burst/request:     {args.cpu:.3f} s")
    print(f"round-robin quantum:   {args.quantum:.3f} s")
    print()
    print(f"one user's offered load:      {single * 100:7.3f}% of one CPU")
    print(f"aggregate offered load:      {load * 100:7.3f}% of one CPU")
    print()
    print("simulated shared CPU")
    print(f"  completed requests:  {metrics.completed}")
    print(f"  mean response time:  {metrics.mean_response:.4f} s")
    print(f"  max response time:   {metrics.max_response:.4f} s")
    print(f"  observed utilization:{metrics.cpu_utilization * 100:7.3f}%")
    print(f"  modeled makespan:    {metrics.makespan:.3f} s")
    print()

    if load < 0.5:
        print(
            "Interpretation: substantial spare CPU capacity remains in this toy workload."
        )
    elif load < 1.0:
        print("Interpretation: the toy workload is busy but below nominal saturation.")
    else:
        print(
            "Interpretation: offered demand reaches/exceeds one CPU; queueing pressure is expected."
        )


if __name__ == "__main__":
    main()
