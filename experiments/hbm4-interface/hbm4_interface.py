print('Synthetic wide-memory interface comparison')
for name, width, rate in [('HBM3E-like', 1024, 9.2), ('HBM4-like', 2048, 11.0)]:
    bandwidth = width * rate / 8.0 / 1000.0
    io_power_proxy = width * (rate ** 1.25) / 1_000_000.0
    print(f'{name:10s} width={width:4d} rate={rate:4.1f} aggregate_proxy={bandwidth:.3f} TB/s power_proxy={io_power_proxy:.3f}')
print('Illustrative calculation only; not vendor electrical data.')
