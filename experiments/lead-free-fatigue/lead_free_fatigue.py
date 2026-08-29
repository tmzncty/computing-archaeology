"""Synthetic solder-fatigue context model. Not an alloy-selection tool."""


def score(alloy_factor, delta_t, geometry_factor):
    return alloy_factor / ((delta_t / 50.0) ** 1.7 * geometry_factor)


def main():
    alloys = {"SnPb-like": 1.00, "SAC-like": 1.15, "other-Pb-free": 0.95}
    scenarios = [("compliant lead", 45, 0.7), ("BGA", 80, 1.0), ("stiff CSP", 110, 1.4)]
    for scenario, dt, geom in scenarios:
        ranked = sorted(((score(f, dt, geom), name) for name, f in alloys.items()), reverse=True)
        print(scenario)
        for value, name in ranked:
            print(f"  {name:14s} synthetic_fatigue_score={value:.3f}")
    print("Factors are invented; rankings are illustrative and context dependent.")


if __name__ == "__main__":
    main()
