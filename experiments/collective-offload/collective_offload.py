print('Synthetic all-reduce traffic comparison')
for nodes in (8, 32, 128):
    payload = 1.0
    endpoint_bytes = 2.0 * (nodes - 1) * payload
    tree_bytes = 2.0 * (nodes - 1) * payload
    endpoint_combine_ops = nodes - 1
    in_network_endpoint_ops = 1
    traffic_reduction_proxy = endpoint_bytes / max(1.0, tree_bytes / 2.0)
    print(f'nodes={nodes:3d} endpoint_ops={endpoint_combine_ops:3d} in_network_endpoint_ops={in_network_endpoint_ops} traffic_reduction_proxy={traffic_reduction_proxy:.2f}')
print('Topology illustration only; not SHARP/NCCL benchmark data.')
