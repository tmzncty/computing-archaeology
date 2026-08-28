"""Synthetic furnace-component contamination budget.

Not calibrated to quartz, SiC, polysilicon, or any commercial material.
"""


def risk(bulk_impurity, surface_factor, outgas_factor, cycle_age):
    age_multiplier = 1.0 + 0.015 * cycle_age
    return bulk_impurity * surface_factor * outgas_factor * age_multiplier


def main():
    cases = [
        ("smooth low-impurity", 0.2, 1.0, 1.0, 20),
        ("porous low-impurity", 0.2, 3.0, 1.2, 20),
        ("aged surface", 0.2, 1.4, 1.1, 100),
        ("clean bulk / dirty surface", 0.1, 4.0, 1.4, 40),
    ]
    for name, bulk, surface, outgas, cycles in cases:
        print(f"{name:27s} synthetic_risk={risk(bulk, surface, outgas, cycles):.4f}")


if __name__ == "__main__":
    main()
