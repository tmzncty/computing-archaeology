"""Synthetic BTI stress/recovery model. Not calibrated to a transistor technology."""


def simulate(stress_fraction, recovery_fraction, steps=1000):
    state = 0.0
    stressed_steps = int(steps * stress_fraction)
    recovery_steps = int(steps * recovery_fraction)
    neutral_steps = max(0, steps - stressed_steps - recovery_steps)
    for _ in range(stressed_steps):
        state += 0.010 * (1.0 - min(state, 0.95))
    for _ in range(recovery_steps):
        state *= 0.992
    for _ in range(neutral_steps):
        state *= 0.998
    return state


def main():
    cases = [
        ("always-biased", 0.95, 0.00),
        ("balanced", 0.50, 0.30),
        ("mostly-recover", 0.20, 0.60),
    ]
    for name, stress, recovery in cases:
        print(f"{name:15s} final_synthetic_degradation={simulate(stress, recovery):.5f}")
    print("Stress/recovery coefficients are invented teaching values.")


if __name__ == "__main__":
    main()
