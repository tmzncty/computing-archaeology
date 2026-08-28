#!/usr/bin/env python3
"""Synthetic contamination-removal model for a cleanroom.

Not CFD and not a reconstruction of Whitfield's room.
"""

SOURCE_PER_STEP = 100.0
FILTER_REMOVAL = {
    "weak_mixing": 0.08,
    "directed_recirculation": 0.70,
}
STEPS = 12

for name, removal in FILTER_REMOVAL.items():
    particles = 0.0
    print(name)
    for step in range(1, STEPS + 1):
        particles += SOURCE_PER_STEP
        particles *= (1.0 - removal)
        print(f"  step {step:2d}: {particles:8.2f} normalized particles")
    print()
