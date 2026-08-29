"""Synthetic semiconductor vacuum-train throughput model."""


def effective_speed(turbo_speed, backing_speed, harsh_penalty=0.0):
    series = 1.0 / (1.0 / turbo_speed + 1.0 / backing_speed)
    return series * (1.0 - harsh_penalty)


def pressure_proxy(gas_load, speed, contamination=0.0):
    return gas_load / max(speed, 1e-9) + contamination


def main():
    cases = [
        ("weak backing", 1000, 120, 0.00, 0.00),
        ("balanced", 1000, 700, 0.00, 0.00),
        ("harsh process", 1000, 700, 0.35, 0.00),
        ("backstream penalty", 1000, 700, 0.00, 0.020),
    ]
    gas_load = 10.0
    for name, turbo, backing, harsh, contam in cases:
        speed = effective_speed(turbo, backing, harsh)
        pressure = pressure_proxy(gas_load, speed, contam)
        print(f"{name:18s} effective_speed={speed:7.2f} pressure_proxy={pressure:8.5f}")


if __name__ == "__main__":
    main()
