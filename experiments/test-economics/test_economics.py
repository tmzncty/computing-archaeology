"""Synthetic ATE economics model: coverage versus test time and salvage."""

def units_per_hour(seconds_per_unit: float) -> float:
    return 3600.0 / seconds_per_unit


def main() -> None:
    scenarios = [
        ("quick screen", 1.0, 0.90),
        ("production test", 3.0, 0.98),
        ("deep characterization", 12.0, 0.995),
    ]
    print("Synthetic automatic-test tradeoff")
    for name, seconds, detection in scenarios:
        print(f"{name:22s} test={seconds:4.1f}s  throughput={units_per_hour(seconds):7.1f}/h  assumed-detection={detection:.1%}")


if __name__ == "__main__":
    main()
