"""Synthetic gate-control geometry proxy; not a transistor simulator."""

geometries = {
    "planar-one-surface": 1.0,
    "double-gate": 2.0,
    "fin-three-surfaces": 3.0,
    "gate-all-around": 4.0,
}
short_channel_pressure = [1.0, 1.5, 2.0, 3.0]

for pressure in short_channel_pressure:
    print(f"short_channel_pressure={pressure:.1f}")
    for name, perimeter in geometries.items():
        control_proxy = perimeter / pressure
        print(f"  {name:20s} control_proxy={control_proxy:5.2f}")
