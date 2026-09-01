#!/usr/bin/env python3
"""Synthetic Flash erase-granularity and wear-distribution model."""

from __future__ import annotations


PAGES_PER_BLOCK = 8
BLOCKS = 8
UPDATES = 128


def naive_updates(updates: int = UPDATES) -> list[int]:
    """Rewrite one logical page in place, erasing its block for every update."""
    erase_counts = [0] * BLOCKS
    for _ in range(updates):
        erase_counts[0] += 1
    return erase_counts


def log_structured_updates(updates: int = UPDATES) -> tuple[list[int], int]:
    """Append versions and reclaim full blocks in round-robin order."""
    erase_counts = [0] * BLOCKS
    physical_page = 0
    for _ in range(updates):
        block = (physical_page // PAGES_PER_BLOCK) % BLOCKS
        offset = physical_page % PAGES_PER_BLOCK
        if offset == 0 and physical_page >= PAGES_PER_BLOCK * BLOCKS:
            erase_counts[block] += 1
        physical_page += 1
    return erase_counts, physical_page


def spread(counts: list[int]) -> int:
    return max(counts) - min(counts)


def main() -> None:
    naive = naive_updates()
    log_counts, physical_writes = log_structured_updates()
    print(f"geometry={BLOCKS}_blocks x {PAGES_PER_BLOCK}_pages updates={UPDATES}")
    print(f"strategy=in_place       erases={sum(naive):2d} max_block_erases={max(naive):2d} spread={spread(naive):2d}")
    print(
        f"strategy=append_reclaim erases={sum(log_counts):2d} max_block_erases={max(log_counts):2d} "
        f"spread={spread(log_counts):2d} physical_writes={physical_writes}"
    )
    print("Counts are synthetic. The model exposes erase-before-reuse and wear placement, not NAND firmware.")


if __name__ == "__main__":
    main()
