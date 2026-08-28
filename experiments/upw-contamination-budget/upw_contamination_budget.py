#!/usr/bin/env python3
"""Synthetic contamination-budget model for semiconductor ultrapure water.

This is not a historical fab specification. It illustrates why excellent ionic
purity alone cannot prove that a water stream is clean enough for wafer use.
"""

STREAMS = {
    "good_resistivity_only": {
        "ions": 0.05,
        "particles": 2.0,
        "organics": 1.4,
        "metals": 0.7,
        "microbial": 0.9,
    },
    "balanced_polishing": {
        "ions": 0.08,
        "particles": 0.25,
        "organics": 0.20,
        "metals": 0.12,
        "microbial": 0.15,
    },
}

LIMIT = 1.0


def evaluate(name, contaminants):
    failures = [k for k, v in contaminants.items() if v > LIMIT]
    print(f"{name}:")
    for key, value in contaminants.items():
        status = "FAIL" if value > LIMIT else "pass"
        print(f"  {key:10s} {value:4.2f}  {status}")
    print("  overall   ", "FAIL" if failures else "pass")
    print()


for stream_name, values in STREAMS.items():
    evaluate(stream_name, values)
