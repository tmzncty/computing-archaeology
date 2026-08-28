#!/usr/bin/env python3
"""Synthetic facility stability budget for a precision process tool."""

CASES = {
    "stable_facility": {"thermal": 0.15, "vibration": 0.20, "power": 0.10},
    "warm_drift": {"thermal": 0.75, "vibration": 0.20, "power": 0.10},
    "vibration_event": {"thermal": 0.15, "vibration": 0.90, "power": 0.10},
    "combined_excursion": {"thermal": 0.60, "vibration": 0.70, "power": 0.45},
}

LIMIT = 1.0

for name, terms in CASES.items():
    rss = sum(v * v for v in terms.values()) ** 0.5
    print(name)
    for key, value in terms.items():
        print(f"  {key:9s}: {value:.2f}")
    print(f"  combined : {rss:.2f}  {'FAIL' if rss > LIMIT else 'pass'}")
    print()

print("Normalized teaching model only; not a lithography or facilities specification.")
