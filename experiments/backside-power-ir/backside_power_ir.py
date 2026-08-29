print('Synthetic power-delivery comparison')
power_w = 200.0
voltage = 0.75
current = power_w / voltage
for name, resistance_mohm in [('frontside', 0.45), ('backside', 0.18)]:
    r = resistance_mohm / 1000.0
    drop = current * r
    loss = current * current * r
    print(f'{name:9s} current={current:7.1f}A drop={drop:6.3f}V loss={loss:7.1f}W')
print('Synthetic teaching parameters; not a chip PDN design.')
