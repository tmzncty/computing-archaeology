"""Synthetic CMP planarity model.

Not calibrated to a real pad, slurry, wafer, or film stack.
"""


def range_of(values):
    return max(values) - min(values)


def uniform_remove(heights, amount):
    return [max(0.0, h - amount) for h in heights]


def density_sensitive_remove(heights, densities, base, sensitivity):
    out = []
    for h, d in zip(heights, densities):
        removal = base * (1.0 + sensitivity * (d - 0.5))
        out.append(max(0.0, h - removal))
    return out


def main():
    heights = [1.0, 1.6, 1.2, 1.9, 1.4, 1.1]
    densities = [0.2, 0.8, 0.4, 0.9, 0.6, 0.3]
    cases = {
        "before": heights,
        "uniform": uniform_remove(heights, 0.7),
        "density-sensitive": density_sensitive_remove(heights, densities, 0.7, 0.5),
    }
    for name, values in cases.items():
        print(f"{name:18s} heights={[round(v, 3) for v in values]} range={range_of(values):.3f}")


if __name__ == "__main__":
    main()
