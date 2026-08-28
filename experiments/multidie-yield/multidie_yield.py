"""Toy monolithic-versus-multidie yield/cost proxy.

Not calibrated to a real node, package, interposer, or chiplet system.
"""

import math


def die_yield(area, defect_density):
    return math.exp(-area * defect_density)


def main():
    total_area = 600.0
    defect_density = 0.0015
    mono_yield = die_yield(total_area, defect_density)

    die_count = 4
    piece_area = total_area / die_count
    piece_yield = die_yield(piece_area, defect_density)
    package_yield = 0.96
    assembled_yield = (piece_yield ** die_count) * package_yield

    print(f"monolithic_die_yield={mono_yield:.4f}")
    print(f"piece_die_yield={piece_yield:.4f}")
    print(f"all_{die_count}_pieces_good_before_assembly={(piece_yield ** die_count):.4f}")
    print(f"assembled_multidie_yield={assembled_yield:.4f}")
    print("\nNote: identical total silicon area makes this deliberately simplistic;")
    print("real economics depend on known-good-die, reuse, process choice, package cost, repair, and much more.")


if __name__ == "__main__":
    main()
