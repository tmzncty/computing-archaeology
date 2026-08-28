#!/usr/bin/env python3
"""Tiny synthetic wafer-yield model for computing archaeology."""

from math import exp, pi

WAFER_DIAMETER_MM = 100.0
WAFER_COST = 100.0  # synthetic currency units
DEFECT_DENSITIES = [0.001, 0.005, 0.01]  # synthetic defects/mm^2
DIE_AREAS = [10, 25, 50, 100, 200]  # mm^2


def gross_die_per_wafer(die_area: float) -> float:
    wafer_area = pi * (WAFER_DIAMETER_MM / 2) ** 2
    # Deliberately crude: ignores edge geometry.
    return wafer_area / die_area


def yield_fraction(defect_density: float, die_area: float) -> float:
    return exp(-defect_density * die_area)


def main() -> None:
    print("Synthetic wafer-yield model")
    print(f"wafer diameter={WAFER_DIAMETER_MM:.0f} mm, wafer cost={WAFER_COST:.1f}\n")
    for density in DEFECT_DENSITIES:
        print(f"defect density={density:.3f}/mm^2")
        print("area  gross-die  yield    good-die  wafer-cost/good")
        for area in DIE_AREAS:
            gross = gross_die_per_wafer(area)
            y = yield_fraction(density, area)
            good = gross * y
            cost = WAFER_COST / good if good else float("inf")
            print(f"{area:4d}  {gross:9.1f}  {y:6.3f}  {good:8.1f}  {cost:15.3f}")
        print()


if __name__ == "__main__":
    main()
