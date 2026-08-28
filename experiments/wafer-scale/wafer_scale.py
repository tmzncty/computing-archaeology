"""Synthetic wafer-area model. Not a manufacturing cost reconstruction."""

import math

DIE_AREA_MM2 = 100.0
YIELD = 0.70
EDGE_EXCLUSION_MM = 5.0

for diameter in (50, 75, 100, 150, 200, 300):
    usable_radius = diameter / 2 - EDGE_EXCLUSION_MM
    usable_area = math.pi * usable_radius**2
    gross = int(usable_area / DIE_AREA_MM2)
    good = int(gross * YIELD)
    print(f"{diameter:3d} mm wafer -> gross~{gross:4d} die, good~{good:4d} at synthetic {YIELD:.0%} yield")