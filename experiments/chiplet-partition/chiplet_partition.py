"""Synthetic die-yield benefit versus chiplet-boundary tax."""

import math

def yield_proxy(area, defect_density=0.003):
    return math.exp(-defect_density * area)

for pieces in (1, 2, 4, 8):
    total_area = 400.0
    die_area = total_area / pieces
    per_die = yield_proxy(die_area)
    silicon_good = per_die ** pieces
    reuse_value = 1.0 + 0.12 * (pieces - 1)
    boundary_tax = 1.0 + 0.06 * (pieces - 1)
    score = silicon_good * reuse_value / boundary_tax
    print(f"pieces={pieces} die_area={die_area:6.1f} all_good={silicon_good:.4f} reuse={reuse_value:.2f} boundary={boundary_tax:.2f} score={score:.4f}")
