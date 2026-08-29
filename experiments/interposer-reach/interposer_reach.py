"""Synthetic wiring-density/reach versus package burden."""

options = [
    ("motherboard", 1.0, 1.0, 1.0),
    ("organic-package", 5.0, 0.45, 1.3),
    ("silicon-interposer", 25.0, 0.15, 2.4),
]
for name, density, distance, burden in options:
    score = density / (distance * burden)
    print(f"{name:18s} density={density:5.1f} distance={distance:.2f} burden={burden:.2f} score={score:7.2f}")
