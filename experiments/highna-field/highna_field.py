"""Synthetic NA resolution benefit versus machine/field burden."""

wavelength = 13.5
for na, burden in ((0.33, 1.0), (0.55, 1.7)):
    resolution_proxy = wavelength / na
    useful_density = 1.0 / resolution_proxy
    system_score = useful_density / burden
    print(f"NA={na:.2f} resolution_proxy={resolution_proxy:.2f} burden={burden:.2f} system_score={system_score:.5f}")
