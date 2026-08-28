#!/usr/bin/env python3
"""Synthetic shared exhaust/abatement capacity model."""

CAPACITY = 100.0
TOOLS = [
    ("etch_1", 22.0),
    ("etch_2", 22.0),
    ("cvd_1", 18.0),
    ("implant_1", 16.0),
    ("clean_1", 12.0),
    ("new_cvd", 20.0),
]

load = 0.0
print(f"shared synthetic capacity: {CAPACITY:.1f}\n")
for name, demand in TOOLS:
    load += demand
    print(f"add {name:10s} demand={demand:5.1f} total={load:6.1f}  {'OVER' if load > CAPACITY else 'ok'}")

print("\nSynthetic teaching model only; not an exhaust or abatement design calculation.")
