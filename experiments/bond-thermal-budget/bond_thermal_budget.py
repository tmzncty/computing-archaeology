"""Synthetic thermal-budget proxy for intermetallic growth risk."""
import math


def risk_proxy(temp_c: float, hours: float) -> float:
    # Deliberately synthetic Arrhenius-like proxy; not a material model.
    return hours * math.exp((temp_c - 100.0) / 35.0)


def main() -> None:
    scenarios = [(125, 1000), (150, 500), (175, 100), (200, 24)]
    print("Synthetic wire-bond thermal-budget proxy")
    for temp, hours in scenarios:
        print(f"{temp:3d} C for {hours:5.0f} h -> proxy={risk_proxy(temp, hours):10.1f}")


if __name__ == "__main__":
    main()
