"""Synthetic LGA contact-array model. Not based on Intel socket limits."""

import random


def simulate(contacts, mean_force, sigma, seed=775):
    rng = random.Random(seed)
    forces = [max(0.0, rng.gauss(mean_force, sigma)) for _ in range(contacts)]
    weak = sum(f < 0.55 for f in forces)
    hot = sum((1.0 / max(f, 0.1)) ** 2 for f in forces[: max(1, contacts // 4)])
    return min(forces), weak, hot


def main():
    for contacts, mean_force, sigma in [(100, 1.0, 0.10), (775, 1.0, 0.10), (775, 0.8, 0.18), (1500, 0.8, 0.18)]:
        minimum, weak, heating = simulate(contacts, mean_force, sigma)
        print(
            f"contacts={contacts:4d} mean={mean_force:.2f} sigma={sigma:.2f} "
            f"min_force={minimum:.3f} weak={weak:3d} power_contact_heat_proxy={heating:8.1f}"
        )
    print("Force thresholds and distributions are invented teaching values.")


if __name__ == "__main__":
    main()
