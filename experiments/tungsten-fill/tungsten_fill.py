"""Synthetic recessed-contact fill model.

Not a CVD kinetics or historical process simulator.
"""


def coverage(mode, depth, width):
    aspect = depth / width
    if mode == "line-of-sight":
        bottom = max(0.05, 1.0 - 0.22 * aspect)
        sidewall = max(0.10, 1.0 - 0.14 * aspect)
    elif mode == "conformal":
        bottom = max(0.65, 0.98 - 0.03 * aspect)
        sidewall = max(0.72, 1.0 - 0.02 * aspect)
    else:  # nucleation + bulk fill
        bottom = max(0.80, 0.995 - 0.015 * aspect)
        sidewall = max(0.82, 0.99 - 0.012 * aspect)
    seam_risk = max(0.0, aspect / 8.0 - min(bottom, sidewall) / 2.0)
    return bottom, sidewall, seam_risk


def main():
    features = [(1, 1), (2, 1), (4, 1), (6, 1)]
    modes = ["line-of-sight", "conformal", "nucleation+bulk"]
    for depth, width in features:
        print(f"feature depth/width={depth}/{width} aspect={depth/width:.1f}")
        for mode in modes:
            b, s, seam = coverage(mode, depth, width)
            print(f"  {mode:17s} bottom={b:5.2f} sidewall={s:5.2f} seam_risk={seam:5.2f}")


if __name__ == "__main__":
    main()
