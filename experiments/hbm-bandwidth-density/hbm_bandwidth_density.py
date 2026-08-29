"""Synthetic wide-near-memory versus narrow-board-memory model."""

interfaces = [
    ("narrow-fast-board", 384, 20.0, 1.00, 1.00),
    ("wide-near-package", 4096, 2.0, 0.35, 0.18),
]
for name, bits, rate, energy, area in interfaces:
    bandwidth = bits * rate
    efficiency = bandwidth / (energy * area)
    print(f"{name:20s} bw_proxy={bandwidth:8.1f} energy={energy:.2f} area={area:.2f} density_eff={efficiency:10.1f}")
