"""Synthetic voltage/current/conduction-loss rack-power proxy."""

power_w = 30000.0
path_resistance = 0.002
connector_resistance = 0.0002
for voltage in (12.0, 48.0):
    current = power_w / voltage
    cable_loss = current ** 2 * path_resistance
    connector_heat = current ** 2 * connector_resistance
    print(f"V={voltage:4.0f} I={current:8.1f}A path_loss={cable_loss:10.1f}W connector_heat={connector_heat:9.1f}W")
