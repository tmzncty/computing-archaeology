"""Synthetic bond-pitch density versus defect/alignment sensitivity."""

for pitch_um in (40, 20, 10, 5, 2):
    density = 1_000_000 / (pitch_um ** 2)
    sensitivity = (10 / pitch_um) ** 1.3 if pitch_um < 10 else 1.0
    usable = density / sensitivity
    print(f"pitch={pitch_um:2d}um density_proxy={density:9.1f} sensitivity={sensitivity:6.2f} usable_proxy={usable:9.1f}")
