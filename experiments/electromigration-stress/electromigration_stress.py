"""Synthetic electromigration relative-lifetime proxy.

Not calibrated to a real process or Black-equation data set.
"""

import math


def relative_lifetime(current_density, temperature_c, n=2.0, activation=0.7):
    k_ev = 8.617333262e-5
    t_k = temperature_c + 273.15
    return (current_density ** -n) * math.exp(activation / (k_ev * t_k))


def main():
    baseline = relative_lifetime(1.0, 80.0)
    cases = [
        ("baseline", 1.0, 80.0),
        ("narrower/higher J", 1.5, 80.0),
        ("hotter", 1.0, 100.0),
        ("hot + high J", 1.5, 100.0),
    ]
    for name, j, temp in cases:
        rel = relative_lifetime(j, temp) / baseline
        print(f"{name:18s} J={j:3.1f} T={temp:5.1f}C relative_life={rel:8.4f}")


if __name__ == "__main__":
    main()
