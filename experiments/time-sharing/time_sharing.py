#!/usr/bin/env python3
"""Toy model for interactive think time and shared CPU demand.

The model does not reproduce CTSS scheduling. It illustrates why many users who
alternate long human think times with short CPU bursts can share one processor
while each still perceives relatively quick service at modest load.
"""

from __future__ import annotations

import argparse
import heapq
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


def reserved_utilization(cpu_burst: float, think_time: float) -> float:
    return cpu_burst / (cpu_burst + think_time)


def offered_load(users: int, cpu_burst: float, think_time: float) -> float:
    return users * reserved_utilization(cpu_burst, think_time)


def build_requests(users: int, rounds: int, think_time: float, cpu_burst: float) -> list[Request]:
    """Create deterministic staggered interactive requests.

    Each user emits a request once per think-time interval. Initial arrivals are
    staggered evenly so all users do not synchronize at t=0.
    """
    requests: list[Request] = []
    spacing = think_time / users if users else 0.0
    for user in range(users):
        first = user * spacing
        for sequence in range(rounds):
            requests.append(
                Request(
                    arrival=first + sequence * think_time,
                    user=user,
                    sequence=sequence,
                    cpu=cpu_burst,
                )
            )
    requests.sort()
    return requests


def simulate_round_robin(
    requests: list[Request], quantum: float
) -> Metrics:
    if quantum <= 0:
        raise ValueError("quantum must be positive")
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
        description="Explore human think time, shared CPU load, and response time."
    )
    parser.add_argument("--users", type=int, default=20)
    parser.add_argument("--rounds", type=int, default=20)
    parser.add_argument("--think", type=float, default=10.0, help="seconds between requests")
    parser.add_argument("--cpu", type=float, default=0.05, help="CPU seconds per request")
    parser.add_argument("--quantum", type=float, default=0.02, help="round-robin quantum seconds")
    args = parser.parse_args()

    if args.users < 1 or args.rounds < 1:
        parser.error("--users and --rounds must be positive")
    if args.think <= 0 or args.cpu <= 0 or args.quantum <= 0:
        parser.error("--think, --cpu, and --quantum must be positive")

    single = reserved_utilization(args.cpu, args.think)
    load = offered_load(args.users, args.cpu, args.think)
    requests = build_requests(args.users, args.rounds, args.think, args.cpu)
    metrics = simulate_round_robin(requests, args.quantum)

    print("Interactive sharing toy model")
    print(f"users:                 {args.users}")
    print(f"requests/user:         {args.rounds}")
    print(f"human think interval:  {args.think:.3f} s")
    print(f"CPU burst/request:     {args.cpu:.3f} s")
    print(f"round-robin quantum:   {args.quantum:.3f} s")
    print()
    print(f"one reserved user's CPU use: {single * 100:7.3f}%")
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
        print("Interpretation: substantial spare CPU capacity remains in this toy workload.")
    elif load < 1.0:
        print("Interpretation: the toy workload is busy but below nominal saturation.")
    else:
        print("Interpretation: offered demand reaches/exceeds one CPU; queueing pressure is expected.")


if __name__ == "__main__":
    main()
