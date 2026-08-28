#!/usr/bin/env python3
"""Synthetic same-layer crossing model for PCB routing intuition."""

from random import Random

RNG = Random(1949)
NETS = 30
POINTS = [(RNG.random(), RNG.random(), RNG.random(), RNG.random()) for _ in range(NETS)]


def orient(ax, ay, bx, by, cx, cy):
    return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)


def crosses(a, b):
    ax, ay, bx, by = a
    cx, cy, dx, dy = b
    return (orient(ax, ay, bx, by, cx, cy) * orient(ax, ay, bx, by, dx, dy) < 0 and
            orient(cx, cy, dx, dy, ax, ay) * orient(cx, cy, dx, dy, bx, by) < 0)


def crossing_count(layers: int) -> int:
    groups = [[] for _ in range(layers)]
    for i, net in enumerate(POINTS):
        groups[i % layers].append(net)
    total = 0
    for group in groups:
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                total += int(crosses(group[i], group[j]))
    return total


def main() -> None:
    print("Synthetic PCB crossing model")
    for layers in [1, 2, 4, 8]:
        print(f"layers={layers:2d}: same-layer geometric crossings={crossing_count(layers)}")
    print("\nExtra layers reduce this toy crossing pressure but add real fabrication cost/complexity.")


if __name__ == "__main__":
    main()
