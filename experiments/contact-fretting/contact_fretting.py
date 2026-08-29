"""Synthetic separable-contact fretting model. Not a connector qualification tool."""


def resistance(cycles, plating_um, force, motion):
    wear = cycles * motion / max(force, 0.1)
    exposed = max(0.0, wear - plating_um * 1200.0)
    oxide = exposed * 0.00008
    base = 0.010 / max(force, 0.2)
    return base + oxide


def main():
    cases = [
        ("thick Au/high force", 0.8, 1.2, 0.4),
        ("thin Au/high force", 0.3, 1.2, 0.4),
        ("thin Au/low force", 0.3, 0.5, 0.4),
        ("thin Au/more motion", 0.3, 1.0, 0.9),
    ]
    for name, plating, force, motion in cases:
        print(name)
        for cycles in [0, 500, 2000, 5000, 10000]:
            r = resistance(cycles, plating, force, motion)
            print(f"  cycles={cycles:5d} R_proxy={r:.4f}")
    print("Wear and resistance coefficients are invented teaching values.")


if __name__ == "__main__":
    main()
