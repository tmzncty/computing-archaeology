"""Synthetic process-line bottleneck model."""

stations = {
    "oxidation/diffusion": 120,
    "lithography": 80,
    "etch": 140,
    "implant": 65,
    "deposition": 100,
    "probe": 110,
}

bottleneck = min(stations, key=stations.get)
for name, wafers_per_hour in stations.items():
    print(f"{name:20s}: {wafers_per_hour:3d} synthetic wafers/hour")
print(f"\nLine throughput cannot exceed bottleneck '{bottleneck}': {stations[bottleneck]} wafers/hour")