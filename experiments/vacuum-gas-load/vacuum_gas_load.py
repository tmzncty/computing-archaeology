#!/usr/bin/env python3
"""Synthetic vacuum gas-load model.

Illustrates why a chamber can have strong pumping and still suffer from a
continuous contamination source such as outgassing or leakage.
"""

PUMP_SPEED = 10.0
INITIAL_GAS = 1000.0
STEPS = 12

SCENARIOS = {
    "clean_decay": 0.0,
    "surface_outgassing": 18.0,
    "small_continuous_leak": 35.0,
}

for name, gas_load in SCENARIOS.items():
    gas = INITIAL_GAS
    print(name)
    for step in range(1, STEPS + 1):
        gas += gas_load
        gas *= 1.0 - (1.0 / PUMP_SPEED)
        print(f"  step {step:2d}: {gas:8.2f} normalized gas")
    print()

print("Synthetic teaching model only; not a vacuum sizing calculation.")
