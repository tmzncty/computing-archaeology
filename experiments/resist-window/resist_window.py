"""Synthetic photoresist process-window model.

Not calibrated to any historical resist, exposure tool, or developer.
"""


def quality(dose, develop):
    exposure_term = max(0.0, 1.0 - abs(dose - 1.0) / 0.55)
    develop_term = max(0.0, 1.0 - abs(develop - 1.0) / 0.50)
    overprocess_penalty = max(0.0, dose - 1.25) * 0.5 + max(0.0, develop - 1.20) * 0.7
    return max(0.0, exposure_term * develop_term - overprocess_penalty)


def main():
    doses = [0.6, 0.8, 1.0, 1.2, 1.4]
    develops = [0.6, 0.8, 1.0, 1.2, 1.4]
    print("synthetic process-window quality")
    for d in doses:
        row = [f"{quality(d, t):.2f}" for t in develops]
        print(f"dose={d:.1f}: " + " ".join(row))


if __name__ == "__main__":
    main()
