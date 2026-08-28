#!/usr/bin/env python3
"""Big/little-endian serialization demonstration."""

from __future__ import annotations


def hex_bytes(data: bytes) -> str:
    return " ".join(f"{b:02X}" for b in data)


def show(value: int, width: int = 4) -> None:
    big = value.to_bytes(width, "big")
    little = value.to_bytes(width, "little")

    print(f"value: 0x{value:0{width * 2}X}")
    print(f"big-endian memory/wire image:    {hex_bytes(big)}")
    print(f"little-endian memory image:      {hex_bytes(little)}")
    print(f"big bytes decoded as little:     0x{int.from_bytes(big, 'little'):0{width * 2}X}")
    print(f"little bytes decoded as big:     0x{int.from_bytes(little, 'big'):0{width * 2}X}")

    network = value.to_bytes(width, "big")
    decoded = int.from_bytes(network, "big")
    assert decoded == value
    print(f"canonical big-endian wire roundtrip: 0x{decoded:0{width * 2}X}")


def main() -> None:
    show(0x12345678)
    print()
    show(0x01020304)
    print("\nThe experiment models representation only; it does not emulate PDP-11 or System/360 hardware.")


if __name__ == "__main__":
    main()
