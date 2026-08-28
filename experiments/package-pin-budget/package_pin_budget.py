#!/usr/bin/env python3
"""Conceptual package pin-budget explorer."""

ADDRESS_BITS = 16
DATA_BITS = 8
CONTROL = 6
POWER_GROUND = 4
PACKAGES = [16, 20, 28, 40]


def main() -> None:
    full = ADDRESS_BITS + DATA_BITS + CONTROL + POWER_GROUND
    muxed = max(ADDRESS_BITS, DATA_BITS) + CONTROL + POWER_GROUND
    serial = 4 + CONTROL + POWER_GROUND  # illustrative serial address/data paths

    print("Conceptual package pin budget")
    print(f"full parallel requirement: {full} pins")
    print(f"address/data multiplexed:   {muxed} pins")
    print(f"highly serialized example:  {serial} pins\n")

    for pins in PACKAGES:
        strategies = []
        if full <= pins:
            strategies.append("full-parallel")
        if muxed <= pins:
            strategies.append("mux-address/data")
        if serial <= pins:
            strategies.append("serialized")
        print(f"package {pins:2d} pins -> {', '.join(strategies) if strategies else 'none of these toy interfaces'}")


if __name__ == "__main__":
    main()
