"""Synthetic thermal-cycle fatigue proxy.

Not calibrated to a real solder alloy or package.
"""


def strain_proxy(cte_mismatch_ppm, delta_t_c):
    return cte_mismatch_ppm * 1e-6 * delta_t_c


def relative_cycles(strain, exponent=2.0):
    return strain ** (-exponent)


def main():
    baseline_strain = strain_proxy(5, 60)
    baseline_cycles = relative_cycles(baseline_strain)
    cases = [
        ("baseline", 5, 60),
        ("bigger deltaT", 5, 100),
        ("bigger mismatch", 9, 60),
        ("both", 9, 100),
    ]
    for name, mismatch, dt in cases:
        strain = strain_proxy(mismatch, dt)
        rel = relative_cycles(strain) / baseline_cycles
        print(f"{name:16s} mismatch={mismatch:2d}ppm/C dT={dt:3d}C relative_cycles={rel:8.4f}")


if __name__ == "__main__":
    main()
