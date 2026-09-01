#!/usr/bin/env python3
"""Synthetic DRAM package-pin and open-row timing model."""

from __future__ import annotations

import math


ROWS = 256
COLUMNS = 256
ACTIVATE_COST = 7
COLUMN_COST = 1
PRECHARGE_COST = 7


def address_pins(rows: int = ROWS, columns: int = COLUMNS) -> tuple[int, int]:
    """Return address pins for direct and row/column-multiplexed addressing."""
    row_bits = math.ceil(math.log2(rows))
    column_bits = math.ceil(math.log2(columns))
    return row_bits + column_bits, max(row_bits, column_bits)


def access_cost(addresses: list[int], columns: int = COLUMNS) -> tuple[int, int, int]:
    """Return synthetic cycles, row activations, and row hits for one-bank accesses."""
    open_row: int | None = None
    cycles = activations = hits = 0
    for address in addresses:
        row = address // columns
        if row != open_row:
            if open_row is not None:
                cycles += PRECHARGE_COST
            cycles += ACTIVATE_COST
            activations += 1
            open_row = row
        else:
            hits += 1
        cycles += COLUMN_COST
    return cycles, activations, hits


def main() -> None:
    direct, multiplexed = address_pins()
    print(f"geometry={ROWS}x{COLUMNS} direct_address_pins={direct} multiplexed_address_pins={multiplexed}")
    traces = {
        "contiguous": list(range(64)),
        "row_stride": [index * COLUMNS for index in range(64)],
        "alternating_rows": [column + (index % 2) * COLUMNS for index, column in enumerate(range(64))],
    }
    for name, trace in traces.items():
        cycles, activations, hits = access_cost(trace)
        print(
            f"trace={name:16s} accesses={len(trace):2d} cycles={cycles:4d} "
            f"activations={activations:2d} row_hits={hits:2d}"
        )
    print("Costs are invented. The model exposes pin reuse and open-row locality, not device timing.")


if __name__ == "__main__":
    main()
