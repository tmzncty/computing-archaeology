"""Synthetic abstraction tradeoff: process detail vs conservative rule margin."""

def effective_density(raw_density: float, safety_margin: float) -> float:
    return raw_density * (1.0 - safety_margin)


def main() -> None:
    raw = 100.0
    print("Synthetic design-rule abstraction model")
    for margin in [0.0, 0.05, 0.10, 0.20, 0.30]:
        density = effective_density(raw, margin)
        print(f"rule margin={margin:4.0%} -> normalized usable density={density:5.1f}")
    print("Trade: conservative rules can reduce density while increasing portability and process safety.")


if __name__ == "__main__":
    main()
