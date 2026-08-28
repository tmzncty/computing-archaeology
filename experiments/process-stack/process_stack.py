#!/usr/bin/env python3
"""Cumulative synthetic process-survival model."""

STEP_COUNTS = [5, 10, 20, 40, 80]
STEP_SURVIVALS = [0.99, 0.995, 0.999]


def main() -> None:
    print("Synthetic cumulative process-stack model\n")
    print("steps  " + "  ".join(f"p={p:.3f}" for p in STEP_SURVIVALS))
    for steps in STEP_COUNTS:
        values = [p**steps for p in STEP_SURVIVALS]
        print(f"{steps:5d}  " + "  ".join(f"{v:7.2%}" for v in values))
    print("\nEach step is treated as independent only for illustration.")


if __name__ == "__main__":
    main()
