"""Synthetic PCB material-stack thermal-mismatch model.

Not calibrated to FR-4, copper, prepreg, solder mask, solder, or any real board.
"""


def expansion(length_mm, cte_ppm, delta_t):
    return length_mm * cte_ppm * 1e-6 * delta_t


def main():
    length = 100.0
    delta_t = 80.0
    materials = [
        ("copper", 17.0),
        ("glass-epoxy x/y", 14.0),
        ("resin-rich region", 45.0),
        ("solder", 24.0),
    ]
    base = expansion(length, materials[0][1], delta_t)
    for name, cte in materials:
        d = expansion(length, cte, delta_t)
        print(f"{name:20s} expansion_mm={d:.4f} mismatch_vs_copper_mm={d-base:+.4f}")


if __name__ == "__main__":
    main()
