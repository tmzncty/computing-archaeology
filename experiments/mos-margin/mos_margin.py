"""Synthetic process-spread model for MOS-like threshold margins."""

import random

random.seed(11)
N = 10000
LOW, HIGH = 0.7, 1.3

for sigma in (0.05, 0.10, 0.20, 0.30):
    values = [random.gauss(1.0, sigma) for _ in range(N)]
    inside = sum(LOW <= v <= HIGH for v in values)
    print(f"sigma={sigma:.2f}: in-window {inside/N:.2%}")

print("Tighter process distributions preserve more design margin.")