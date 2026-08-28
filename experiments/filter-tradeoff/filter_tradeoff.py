"""Synthetic filtration capture / pressure-drop / loading tradeoff.

Not calibrated to any real HEPA, ULPA, membrane, depth, gas, or CMP filter.
"""


def performance(retention, loading):
    capture = retention * (1.0 - 0.08 * loading)
    pressure_drop = 0.3 + retention ** 2 * 1.6 + loading * 0.9
    useful_flow = 1.0 / pressure_drop
    return max(0.0, capture), pressure_drop, useful_flow


def main():
    for retention in [0.6, 0.8, 0.95]:
        for loading in [0.0, 0.5, 1.0]:
            capture, dp, flow = performance(retention, loading)
            print(
                f"retention={retention:.2f} loading={loading:.1f} "
                f"capture_proxy={capture:.3f} pressure_drop={dp:.3f} flow_proxy={flow:.3f}"
            )


if __name__ == "__main__":
    main()
