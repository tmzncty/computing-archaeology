"""Synthetic wafer-stage radial thermal-uniformity model."""


def temperatures(stage_temp=70.0, contact=[1.0, 0.95, 0.85, 0.70], plasma_heat=[6, 7, 8, 9]):
    result = []
    for c, heat in zip(contact, plasma_heat):
        result.append(stage_temp + heat / c)
    return result


def main():
    for name, contact in [("uniform-contact", [1,1,1,1]), ("edge-loss", [1.0,0.95,0.85,0.70])]:
        temps = temperatures(contact=contact)
        spread = max(temps) - min(temps)
        print(f"{name:16s} temps={[round(t,2) for t in temps]} spread={spread:5.2f}C")


if __name__ == "__main__":
    main()
