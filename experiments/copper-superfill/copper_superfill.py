"""Synthetic conformal versus bottom-up copper fill model."""


def simulate(depth=10, steps=8, bottom_gain=0.0):
    profile = [0.0] * depth
    for _ in range(steps):
        for i in range(depth):
            gain = 1.0 + bottom_gain * (i / max(depth - 1, 1))
            profile[i] += gain
    seam_risk = max(profile[0] - profile[-1], 0.0)
    bottom_fill = profile[-1]
    top_fill = profile[0]
    return top_fill, bottom_fill, seam_risk


def main():
    for name, gain in [("conformal", 0.0), ("mild-superfill", 0.5), ("strong-superfill", 1.2)]:
        top, bottom, seam = simulate(bottom_gain=gain)
        print(f"{name:16s} top={top:6.2f} bottom={bottom:6.2f} seam_risk_proxy={seam:6.2f}")


if __name__ == "__main__":
    main()
