print('Synthetic coolant-condition window')
scenarios = {
    'balanced': (0.15, 0.10, 0.10, 0.95),
    'corrosive': (0.80, 0.15, 0.10, 0.92),
    'fouled': (0.20, 0.20, 0.75, 0.72),
    'conductive': (0.25, 0.85, 0.20, 0.90),
}
for name, (corrosion, conductivity, fouling, heat_transfer) in scenarios.items():
    risk = 0.35 * corrosion + 0.25 * conductivity + 0.25 * fouling + 0.15 * (1 - heat_transfer)
    print(f'{name:10s} risk_proxy={risk:.3f} heat_transfer={heat_transfer:.2f} status={"pass" if risk < 0.35 else "review"}')
print('Synthetic condition score; not a coolant specification.')
