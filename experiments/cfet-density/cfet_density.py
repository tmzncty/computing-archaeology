print('Synthetic standard-cell footprint comparison')
styles = [
    ('side-by-side GAA', 1.00, 1.00),
    ('forksheet-like', 0.82, 1.10),
    ('stacked CFET', 0.58, 1.35),
]
for name, area, integration_penalty in styles:
    effective = area * integration_penalty
    density = 1.0 / effective
    print(f'{name:16s} geometric_area={area:.2f} integration_penalty={integration_penalty:.2f} density_proxy={density:.3f}')
print('Synthetic geometry only; not a transistor PPA forecast.')
