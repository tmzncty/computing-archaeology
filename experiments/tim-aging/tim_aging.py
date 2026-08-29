"""Synthetic thermal-interface aging model. Not a service-life predictor."""


def resistance(cycles, pump_rate, dry_rate, initial=0.08):
    pump = pump_rate * (cycles / 1000.0) ** 0.8
    dry = dry_rate * (cycles / 1000.0) ** 1.15
    return initial * (1.0 + pump + dry)


def main():
    materials = [
        ("stable", 0.03, 0.02),
        ("pump-out prone", 0.18, 0.03),
        ("dry-out prone", 0.04, 0.16),
    ]
    for name, pump, dry in materials:
        print(name)
        for cycles in [0, 100, 1000, 5000, 10000]:
            r = resistance(cycles, pump, dry)
            print(f"  cycles={cycles:5d} R_proxy={r:.4f}")
    print("Aging coefficients are invented; not a TIM qualification model.")


if __name__ == "__main__":
    main()
