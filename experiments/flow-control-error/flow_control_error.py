"""Synthetic gas-flow-control error model.

Not calibrated to any historical or commercial MFC.
"""


def delivered_dose(setpoint, duration, bias, response_fraction):
    effective_flow = setpoint * (1.0 + bias)
    transient_loss = effective_flow * duration * (1.0 - response_fraction) * 0.25
    return effective_flow * duration - transient_loss


def main():
    setpoint = 100.0
    duration = 10.0
    commanded = setpoint * duration
    cases = [
        ("ideal", 0.0, 1.0),
        ("+2% bias", 0.02, 1.0),
        ("slow response", 0.0, 0.75),
        ("bias + slow", -0.02, 0.75),
    ]
    print(f"commanded_dose={commanded:.2f}")
    for name, bias, response in cases:
        delivered = delivered_dose(setpoint, duration, bias, response)
        error = (delivered - commanded) / commanded * 100.0
        print(f"{name:14s} delivered={delivered:.2f} error={error:+.2f}%")


if __name__ == "__main__":
    main()
