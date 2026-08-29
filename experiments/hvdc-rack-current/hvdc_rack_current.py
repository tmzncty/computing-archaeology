print('Synthetic rack distribution current')
power_kw = 1000.0
for voltage in (48, 400, 800):
    current = power_kw * 1000.0 / voltage
    conductor_loss_proxy = current * current * 1e-6
    print(f'{voltage:4d} V -> {current:8.1f} A, I^2R proxy={conductor_loss_proxy:9.2f}')
print('Same-power comparison only; not an HVDC safety or conductor design.')
