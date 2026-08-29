"""Synthetic backside-helium wafer thermal-interface model."""


def zone_temperature(power, chuck_temp, coupling, leak_penalty=0.0):
    effective = max(0.05, coupling * (1.0 - leak_penalty))
    return chuck_temp + power / effective


def main():
    chuck = 20.0
    power = 10.0
    zones = [
        ("center-good", 1.00, 0.00),
        ("mid-good", 0.92, 0.02),
        ("edge-small-leak", 0.88, 0.18),
        ("edge-large-leak", 0.82, 0.35),
    ]
    for name, coupling, leak in zones:
        t = zone_temperature(power, chuck, coupling, leak)
        print(f"{name:18s} coupling={coupling:4.2f} leak={leak:4.2f} wafer_temp={t:6.2f}")


if __name__ == "__main__":
    main()
