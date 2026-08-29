from math import exp

print('Synthetic EUV throughput/stochastic tradeoff')
for dose in (20, 30, 40, 60):
    for transmission in (0.90, 0.97):
        photons = dose * transmission
        stochastic_fail = exp(-photons / 12.0)
        throughput_proxy = 1000.0 / dose
        useful = throughput_proxy * (1.0 - stochastic_fail)
        print(f'dose={dose:2d} transmission={transmission:.2f} fail={stochastic_fail:.4f} useful_proxy={useful:.2f}')
print('Synthetic values only; not a scanner or resist model.')
