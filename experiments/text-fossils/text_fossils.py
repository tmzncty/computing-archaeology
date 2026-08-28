#!/usr/bin/env python3
"""Tiny CR/LF and ASCII/EBCDIC teaching model."""

from __future__ import annotations


def simulate_controls(stream: str) -> tuple[int, int]:
    row = 0
    col = 0
    for char in stream:
        if char == "\r":
            col = 0
        elif char == "\n":
            row += 1
        else:
            col += 1
    return row, col


def show_encoding(text: str) -> None:
    ascii_bytes = text.encode("ascii")
    ebcdic_bytes = text.encode("cp037")
    print(f"text:   {text!r}")
    print("ASCII: ", " ".join(f"{b:02X}" for b in ascii_bytes))
    print("EBCDIC:", " ".join(f"{b:02X}" for b in ebcdic_bytes))


def main() -> None:
    cases = {
        "CR only": "ABC\r",
        "LF only": "ABC\n",
        "CRLF": "ABC\r\n",
        "LFCR": "ABC\n\r",
    }

    print("Separate carriage-return / line-feed motions")
    for name, stream in cases.items():
        row, col = simulate_controls(stream)
        print(f"{name:<8} -> row={row}, column={col}")

    print("\nSame glyphs, different encoded bytes")
    show_encoding("ABC123")

    ascii_order = sorted("A1a", key=lambda c: c.encode("ascii")[0])
    ebcdic_order = sorted("A1a", key=lambda c: c.encode("cp037")[0])
    print("\nByte-order sort of A, 1, a")
    print("ASCII :", ascii_order)
    print("EBCDIC:", ebcdic_order)

    print("\nPython cp037 is used only as a modern codec demonstration, not as proof of every historical EBCDIC variant.")


if __name__ == "__main__":
    main()
