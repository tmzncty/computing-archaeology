"""Synthetic low-k interconnect vs high-k gate objective model."""


def wire_capacitance_proxy(k, spacing=1.0):
    return k / spacing


def gate_capacitance_proxy(k, thickness):
    return k / thickness


def leakage_proxy(thickness):
    # Synthetic exponential sensitivity, not a tunneling equation.
    return 2.71828 ** (-2.0 * thickness)


def main():
    print("interconnect objective: lower k lowers capacitive proxy")
    for k in (4.0, 3.0, 2.5, 2.0):
        print(f"  k={k:3.1f} wire_cap_proxy={wire_capacitance_proxy(k):5.2f}")

    print("\ngate objective: higher k permits thicker physical film at fixed capacitance proxy")
    target_c = 2.0
    for k in (3.9, 8.0, 16.0, 24.0):
        thickness = k / target_c
        print(
            f"  k={k:4.1f} thickness={thickness:5.2f} "
            f"cap_proxy={gate_capacitance_proxy(k, thickness):4.1f} "
            f"leakage_proxy={leakage_proxy(thickness):.6f}"
        )


if __name__ == "__main__":
    main()
