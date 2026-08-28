"""Synthetic chemically amplified resist gain/blur model."""


def result(photon_events, gain, diffusion):
    reacted = photon_events * gain
    blur = gain * diffusion
    fidelity = reacted / (1.0 + blur)
    return reacted, blur, fidelity


def main():
    for gain, diffusion in [(1, 0.02), (5, 0.03), (20, 0.04), (50, 0.08)]:
        reacted, blur, fidelity = result(100, gain, diffusion)
        print(f"gain={gain:3d} reacted={reacted:6.0f} blur_proxy={blur:6.2f} fidelity_proxy={fidelity:8.2f}")


if __name__ == "__main__":
    main()
