print('Synthetic per-lane channel budget as rate rises')
for rate in (112, 224, 448):
    nyquist_proxy = rate / 2.0
    material_loss = 0.040 * nyquist_proxy
    package_loss = 0.018 * nyquist_proxy
    equalization_power = (rate / 112.0) ** 1.6
    margin = 18.0 - material_loss - package_loss
    print(f'rate={rate:3d} loss={material_loss + package_loss:5.2f}dB margin_proxy={margin:5.2f} eq_power_proxy={equalization_power:4.2f}')
print('Synthetic values; not OIF compliance limits.')
