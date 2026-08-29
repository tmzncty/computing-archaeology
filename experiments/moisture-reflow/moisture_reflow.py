"""Synthetic moisture/reflow package-stress model. Not an MSL classifier."""

import math


def moisture(exposure_hours, humidity_factor):
    return 1.0 - math.exp(-exposure_hours * humidity_factor / 48.0)


def stress(moisture_level, peak_temp_c, mismatch):
    return moisture_level * max(0.0, peak_temp_c - 100.0) * mismatch


def main():
    cases = [
        ("dry packed", 0.5, 0.2, 245, 1.0),
        ("short floor", 8, 0.5, 245, 1.0),
        ("long humid", 96, 0.9, 245, 1.0),
        ("baked recovery", 2, 0.2, 245, 1.0),
    ]
    for name, hours, humid, temp, mismatch in cases:
        m = moisture(hours, humid)
        print(f"{name:15s} moisture_proxy={m:.3f} reflow_stress_proxy={stress(m,temp,mismatch):7.2f}")
    print("Synthetic teaching values only; not J-STD-020/033 classification.")


if __name__ == "__main__":
    main()
