#!/usr/bin/env python3
"""Synthetic impurity accumulation in a high-purity gas path."""

SOURCE_IMPURITY_PPB = 1.0
COMPONENT_ADDITIONS_PPB = [
    ("regulator", 0.4),
    ("valve", 0.2),
    ("welded_tube_run", 0.3),
    ("manifold", 0.5),
    ("tool_hookup", 0.4),
]

impurity = SOURCE_IMPURITY_PPB
print(f"source: {impurity:.2f} ppb synthetic impurity")
for name, addition in COMPONENT_ADDITIONS_PPB:
    impurity += addition
    print(f"after {name:16s}: {impurity:.2f} ppb")

print("\nThis is a teaching model, not a semiconductor gas specification.")
