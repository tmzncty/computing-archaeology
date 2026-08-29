"""Synthetic level-spacing and coding-recovery proxy; not PCIe FEC."""

full_scale = 1.0
noise_levels = (0.03, 0.06, 0.10, 0.14)
for scheme, levels, bits_per_symbol in (("NRZ", 2, 1), ("PAM4", 4, 2)):
    spacing = full_scale / (levels - 1)
    print(scheme)
    for noise in noise_levels:
        raw_margin = max(0.0, spacing - 2 * noise)
        coding_proxy = min(1.0, raw_margin / spacing + (0.18 if scheme == "PAM4" else 0.02))
        throughput_proxy = bits_per_symbol * coding_proxy
        print(f"  noise={noise:.2f} spacing={spacing:.3f} margin={raw_margin:.3f} throughput_proxy={throughput_proxy:.3f}")
