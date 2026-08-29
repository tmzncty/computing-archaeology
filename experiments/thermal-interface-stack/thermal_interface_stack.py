"""Synthetic processor package thermal-interface resistance chain."""


def layer_r(thickness, conductivity, void_fraction=0.0):
    effective_k = max(0.05, conductivity * (1.0 - 0.85 * void_fraction))
    return thickness / effective_k


def main():
    fixed = 0.12  # synthetic die + lid + cooler resistance contribution
    cases = [
        ("thin-good", 0.08, 1.0, 0.00),
        ("thick-good", 0.20, 1.0, 0.00),
        ("thin-voided", 0.08, 1.0, 0.35),
        ("thick-voided", 0.20, 1.0, 0.35),
    ]
    power = 100.0
    for name, thickness, k, voids in cases:
        tim_r = layer_r(thickness, k, voids)
        total_r = fixed + tim_r
        rise = power * total_r
        print(f"{name:13s} tim_R={tim_r:6.3f} total_R={total_r:6.3f} temp_rise_proxy={rise:7.2f}")


if __name__ == "__main__":
    main()
