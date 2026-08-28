"""Synthetic sputter-target erosion/utilization model.

Not calibrated to a commercial cathode or target.
"""


def utilization(profile, retirement_depth):
    remaining = [max(retirement_depth - d, 0.0) for d in profile]
    used = sum(min(d, retirement_depth) for d in profile)
    capacity = len(profile) * retirement_depth
    return used / capacity, remaining


def main():
    cases = {
        "uniform": [4, 4, 4, 4, 4, 4, 4, 4],
        "racetrack": [1, 2, 5, 8, 10, 8, 5, 2],
        "sharper": [1, 1, 3, 7, 10, 7, 3, 1],
    }
    retirement_depth = 10
    for name, profile in cases.items():
        util, remaining = utilization(profile, retirement_depth)
        deepest = max(profile)
        print(f"{name:10s} deepest={deepest:4.1f} utilization={util*100:6.2f}% remaining_mass_proxy={sum(remaining):6.1f}")


if __name__ == "__main__":
    main()
