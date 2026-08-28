#!/usr/bin/env python3
"""Synthetic mask-overlay survival model."""

from random import Random

RNG = Random(1959)
TRIALS = 10_000
LAYERS = [2, 4, 8, 16]
SIGMAS = [0.05, 0.10, 0.20]  # synthetic position units
TOLERANCE = 0.25


def survives(layer_count: int, sigma: float) -> bool:
    for _ in range(layer_count):
        x = RNG.gauss(0.0, sigma)
        y = RNG.gauss(0.0, sigma)
        if abs(x) > TOLERANCE or abs(y) > TOLERANCE:
            return False
    return True


def main() -> None:
    print("Synthetic lithography overlay model")
    print(f"tolerance=±{TOLERANCE:.2f} synthetic units, trials={TRIALS}\n")
    for sigma in SIGMAS:
        print(f"overlay sigma={sigma:.2f}")
        for layers in LAYERS:
            ok = sum(survives(layers, sigma) for _ in range(TRIALS))
            print(f"  layers={layers:2d}: survival={ok / TRIALS:6.2%}")
        print()


if __name__ == "__main__":
    main()
