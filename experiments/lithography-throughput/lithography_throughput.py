"""Synthetic lithography throughput / field-count model."""

def wafers_per_hour(fields: int, exposure_s: float, overhead_s: float) -> float:
    seconds = fields * exposure_s + overhead_s
    return 3600.0 / seconds


def main() -> None:
    print("Synthetic step-and-repeat throughput model")
    scenarios = [
        (40, 0.20, 20.0),
        (80, 0.20, 20.0),
        (80, 0.50, 20.0),
        (120, 0.50, 30.0),
    ]
    for fields, exp, overhead in scenarios:
        print(
            f"fields={fields:3d} exposure={exp:4.2f}s overhead={overhead:4.0f}s -> {wafers_per_hour(fields, exp, overhead):6.1f} wafers/h"
        )


if __name__ == "__main__":
    main()
