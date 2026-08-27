#!/usr/bin/env python3
"""Compare field/character packing across historical word sizes."""

from __future__ import annotations

import argparse


def parse_csv_ints(text: str) -> list[int]:
    values = [int(part.strip()) for part in text.split(",") if part.strip()]
    if not values or any(value <= 0 for value in values):
        raise argparse.ArgumentTypeError("provide comma-separated positive integers")
    return values


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Show how several field widths pack into several machine word widths."
    )
    parser.add_argument(
        "--words",
        type=parse_csv_ints,
        default=parse_csv_ints("18,24,36,48,60,64"),
        help="comma-separated word widths",
    )
    parser.add_argument(
        "--fields",
        type=parse_csv_ints,
        default=parse_csv_ints("5,6,7,8,9,12"),
        help="comma-separated field/character widths",
    )
    args = parser.parse_args()

    print("word field fields/word unused exact symbols/field")
    print("---- ----- ----------- ------ ----- -------------")
    for word in args.words:
        for field in args.fields:
            count, unused = divmod(word, field)
            exact = "yes" if unused == 0 else "no"
            symbols = 1 << field
            print(
                f"{word:>4} {field:>5} {count:>11} {unused:>6} "
                f"{exact:>5} {symbols:>13}"
            )
        print()

    print(
        "Packing efficiency is only one design pressure. This table does not model "
        "address fields, arithmetic precision, circuit cost, I/O formats, or compatibility."
    )


if __name__ == "__main__":
    main()
