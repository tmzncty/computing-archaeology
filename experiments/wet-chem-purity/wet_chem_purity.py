"""Synthetic multi-channel chemical-purity budget.

Not a semiconductor chemical specification or safety tool.
"""

CHANNELS = {
    "metals": (0.4, 0.2),
    "particles": (0.3, 0.1),
    "organics": (0.2, 0.25),
    "moisture": (0.1, 0.15),
}


def score(channels):
    total = 0.0
    for name, (weight, limit) in CHANNELS.items():
        value = channels[name]
        total += weight * min(value / limit, 5.0)
    return total


def main():
    cases = {
        "balanced": {"metals": 0.08, "particles": 0.05, "organics": 0.08, "moisture": 0.05},
        "great assay bad metals": {"metals": 0.35, "particles": 0.03, "organics": 0.03, "moisture": 0.03},
        "clean bulk dirty delivery": {"metals": 0.08, "particles": 0.22, "organics": 0.09, "moisture": 0.05},
    }
    for name, channels in cases.items():
        print(f"{name:26s} synthetic_risk={score(channels):.3f}")


if __name__ == "__main__":
    main()
