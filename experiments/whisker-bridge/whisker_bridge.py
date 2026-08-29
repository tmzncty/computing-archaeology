"""Synthetic long-tail whisker bridge model. Not a growth predictor."""

import random


def bridges(spacing_mm, samples=10000, seed=1998):
    rng = random.Random(seed)
    count = 0
    longest = 0.0
    for _ in range(samples):
        # Invented heavy-tailed mixture: most are short, a few are much longer.
        if rng.random() < 0.985:
            length = rng.expovariate(1 / 0.08)
        else:
            length = rng.expovariate(1 / 0.8)
        longest = max(longest, length)
        if length >= spacing_mm:
            count += 1
    return count, longest


def main():
    for spacing in [2.0, 1.0, 0.5, 0.25]:
        count, longest = bridges(spacing)
        print(f"spacing={spacing:4.2f}mm bridges={count:4d}/10000 longest={longest:5.2f}mm")
    print("Distribution is invented; it demonstrates rare long-tail bridging only.")


if __name__ == "__main__":
    main()
