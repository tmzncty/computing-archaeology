#!/usr/bin/env python3
"""Synthetic static-charge risk model.

Separates a direct ESD-like damage channel from electrostatic particle attraction.
"""

CHARGE_LEVELS = [0.0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0]

print("charge  esd_risk  particle_attraction")
for charge in CHARGE_LEVELS:
    esd_risk = min(1.0, charge ** 2 / 2.0)
    attraction = charge ** 1.5
    print(f"{charge:5.2f}   {esd_risk:6.3f}        {attraction:6.3f}")

print("\nSynthetic normalized model only; not an ESD qualification method.")
