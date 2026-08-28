"""Synthetic contamination-exposure budget for open vs podded handling."""

def exposure(rate: float, minutes: float, area: float) -> float:
    return rate * minutes * area


def main() -> None:
    scenarios = [
        ("open cassette", 1.0, 30.0, 1.0),
        ("short open transfer", 1.0, 5.0, 1.0),
        ("sealed pod + local transfer", 0.1, 5.0, 1.0),
    ]
    print("Synthetic contamination exposure proxy")
    for name, rate, minutes, area in scenarios:
        print(f"{name:28s} proxy={exposure(rate, minutes, area):6.2f}")


if __name__ == "__main__":
    main()
