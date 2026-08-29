"""Synthetic high-speed PCB material model. Not an EM field solver."""

import math


def conductor_loss(freq_ghz, roughness):
    skin_like = math.sqrt(freq_ghz)
    return skin_like * (1.0 + 0.45 * roughness)


def skew(length_in, glass_fraction_a, glass_fraction_b, contrast=5.0):
    return length_in * abs(glass_fraction_a - glass_fraction_b) * contrast


def main():
    print("roughness / frequency loss proxy")
    for f in [1, 5, 10, 25]:
        smooth = conductor_loss(f, 0.1)
        rough = conductor_loss(f, 1.0)
        print(f"  {f:2d} GHz smooth={smooth:6.3f} rough={rough:6.3f}")

    print("\nglass-weave differential skew proxy")
    for name, a, b in [("balanced",0.50,0.50),("mild",0.55,0.45),("bad alignment",0.80,0.20)]:
        print(f"  {name:13s} skew_proxy={skew(8,a,b):6.2f} ps-like units")
    print("All units/factors are invented; this is not a transmission-line solver.")


if __name__ == "__main__":
    main()
