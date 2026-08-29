"""Synthetic underfill thermal-mismatch load-sharing model."""


def mismatch_strain(cte_delta, delta_t):
    return cte_delta * delta_t


def stress_channels(mismatch, coupling):
    bump_strain = mismatch * (1.0 - 0.75 * coupling)
    die_stack_stress = mismatch * (0.20 + 0.95 * coupling**1.6)
    return bump_strain, die_stack_stress


def main():
    mismatch = mismatch_strain(1.0, 1.0)
    cases = [
        ("no underfill", 0.00),
        ("soft", 0.30),
        ("moderate", 0.60),
        ("very stiff", 0.95),
    ]
    for name, coupling in cases:
        bump, stack = stress_channels(mismatch, coupling)
        print(f"{name:12s} coupling={coupling:4.2f} bump_strain={bump:5.3f} die_stack_stress={stack:5.3f}")


if __name__ == "__main__":
    main()
