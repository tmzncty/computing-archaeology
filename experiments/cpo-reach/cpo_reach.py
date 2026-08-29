print('Synthetic electrical-reach pressure before optical handoff')
for electrical_cm in (2, 5, 10, 20, 40):
    loss_db = 0.32 * electrical_cm
    equalizer_power = 0.05 * (loss_db ** 1.7)
    cpo_total = 1.2 + 0.08 * electrical_cm
    pluggable_total = equalizer_power + 0.9
    preferred = 'CPO-like' if cpo_total < pluggable_total else 'front-panel optics'
    print(f'reach={electrical_cm:2d}cm loss={loss_db:5.2f}dB electrical_path_power={pluggable_total:5.2f} cpo_proxy={cpo_total:5.2f} -> {preferred}')
print('Synthetic tradeoff only; not an optical or SerDes link budget.')
