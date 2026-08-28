"""Synthetic fixed-vs-variable manufacturing boundary model."""

OWN_FAB_FIXED = 100_000_000
OWN_FAB_VARIABLE = 8
FOUNDRY_VARIABLE = 28

for volume in (10_000, 100_000, 1_000_000, 10_000_000):
    own = OWN_FAB_FIXED + volume * OWN_FAB_VARIABLE
    foundry = volume * FOUNDRY_VARIABLE
    print(
        f"volume={volume:>10,}: own-fab={own:>12,.0f}  "
        f"foundry={foundry:>12,.0f}  cheaper={'own fab' if own < foundry else 'foundry'}"
    )

print("\nAll costs are synthetic; the point is fixed-cost structure, not historical pricing.")