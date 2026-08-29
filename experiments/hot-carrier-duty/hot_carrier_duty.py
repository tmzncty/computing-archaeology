"""Synthetic hot-carrier duty-cycle model. Not calibrated to a real MOS process."""


def damage(field_stress, duty, temperature_c, hours):
    thermal = 1.0 + max(0.0, temperature_c - 40.0) / 60.0
    return (field_stress ** 2.2) * duty * thermal * hours


def main():
    cases = [
        ("light switching", 0.55, 0.10, 60, 10000),
        ("heavy switching", 0.80, 0.65, 60, 10000),
        ("hot heavy", 0.80, 0.65, 95, 10000),
        ("short severe", 1.00, 0.90, 80, 2000),
    ]
    baseline = damage(*cases[0][1:])
    for name, field, duty, temp, hours in cases:
        d = damage(field, duty, temp, hours)
        print(f"{name:16s} synthetic_damage={d:10.1f} relative={d/baseline:7.2f}x")
    print("Equal wall-clock time does not imply equal stress history.")


if __name__ == "__main__":
    main()
