"""Synthetic CAF risk-path model. Not an IPC qualification method."""


def risk(spacing_mm, humidity, voltage, damage):
    gradient = voltage / spacing_mm
    return humidity * gradient * (1.0 + 2.5 * damage)


def main():
    cases = [
        ("wide/dry", 0.80, 0.35, 12, 0.1),
        ("tight/dry", 0.25, 0.35, 12, 0.1),
        ("tight/humid", 0.25, 0.90, 12, 0.1),
        ("tight/humid/damaged", 0.25, 0.90, 12, 0.8),
    ]
    for name, spacing, humidity, voltage, damage in cases:
        print(f"{name:22s} synthetic_CAF_risk={risk(spacing,humidity,voltage,damage):8.2f}")
    print("All factors are invented; use IPC CAF methods for real qualification.")


if __name__ == "__main__":
    main()
