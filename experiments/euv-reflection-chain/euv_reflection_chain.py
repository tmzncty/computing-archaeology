"""Synthetic reflective optical-train throughput proxy."""

for reflectivity in (0.60, 0.65, 0.70, 0.75):
    for mirrors in (6, 8, 10):
        transmission = reflectivity ** mirrors
        print(f"R={reflectivity:.2f} mirrors={mirrors:2d} chain_proxy={transmission:.5f}")
    print()
