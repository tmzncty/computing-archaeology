"""Synthetic alpha-particle soft-error threshold model."""

import random


def upset_count(critical_charge, events=5000, seed=1979):
    rng = random.Random(seed)
    upset = 0
    for _ in range(events):
        deposited = rng.expovariate(1 / 1.0)
        if deposited >= critical_charge:
            upset += 1
    return upset


def main():
    for qcrit in [2.0, 1.5, 1.0, 0.7, 0.5]:
        upsets = upset_count(qcrit)
        print(f"critical_charge={qcrit:3.1f} synthetic_upsets={upsets:4d}/5000")
    print("Event distribution and charge units are invented; this is not radiation transport.")


if __name__ == "__main__":
    main()
