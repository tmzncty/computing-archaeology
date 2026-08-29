"""Synthetic parallel cold-plate flow imbalance model."""

loads = [700, 700, 500, 500]
flow_sets = [
    ("balanced", [1.0, 1.0, 0.8, 0.8]),
    ("one-restricted", [1.0, 0.45, 0.8, 0.8]),
]
for name, flows in flow_sets:
    rises = [load / (flow * 100.0) for load, flow in zip(loads, flows)]
    print(f"{name:14s} total_flow={sum(flows):.2f} local_rise_proxy={[round(x,2) for x in rises]} max={max(rises):.2f}")
