"""Synthetic CMP pad glazing/conditioning balance model."""


def state(conditioning, glazing_rate=1.0):
    texture = max(0.0, 10.0 - glazing_rate * 8 + conditioning * 7)
    pad_wear = conditioning * 5
    stability = max(0.0, min(texture, 10.0) - 0.2 * pad_wear)
    return texture, pad_wear, stability


def main():
    for c in [0.0, 0.4, 0.8, 1.2, 1.8]:
        texture, wear, stability = state(c)
        print(f"conditioning={c:3.1f} texture={texture:6.2f} wear={wear:6.2f} stability_proxy={stability:6.2f}")


if __name__ == "__main__":
    main()
