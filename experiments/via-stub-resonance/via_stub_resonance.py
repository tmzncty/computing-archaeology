"""Synthetic via-stub quarter-wave resonance proxy. Not a full PCB via model."""

C = 299_792_458.0


def notch_ghz(stub_mm, er):
    length_m = stub_mm / 1000.0
    return C / (4.0 * length_m * (er ** 0.5)) / 1e9


def main():
    er = 4.0
    for stub in [4.0, 2.5, 1.5, 0.8, 0.25, 0.10]:
        print(f"stub={stub:4.2f} mm first_quarter_wave_proxy={notch_ghz(stub,er):7.2f} GHz")
    print("Simple open-stub proxy only; pads, anti-pads, return paths and loss are omitted.")


if __name__ == "__main__":
    main()
