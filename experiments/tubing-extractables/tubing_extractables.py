"""Synthetic high-purity fluid-path contamination accumulator.

Not calibrated to any real tubing, fitting, valve, resin, or chemical.
"""


def delivered_purity(source_contam, component_additions):
    total = source_contam
    history = [("source", total)]
    for name, addition in component_additions:
        total += addition
        history.append((name, total))
    return history


def main():
    path = [
        ("tank", 0.010),
        ("tube-1", 0.004),
        ("valve", 0.012),
        ("filter housing", 0.006),
        ("tube-2", 0.004),
        ("dispense fitting", 0.009),
    ]
    for name, total in delivered_purity(0.020, path):
        print(f"{name:18s} cumulative_synthetic_contamination={total:.3f}")


if __name__ == "__main__":
    main()
