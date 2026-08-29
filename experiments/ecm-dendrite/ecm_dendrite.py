"""Synthetic PCB electrochemical-migration / dendrite model."""


def growth(humidity, contamination, voltage, spacing, steps=12):
    length = 0.0
    history = []
    for step in range(1, steps + 1):
        length += 0.015 * humidity * contamination * voltage / spacing
        bridged = length >= spacing
        fused = bridged and step % 3 == 0
        if fused:
            length *= 0.35
        history.append((step, length, bridged, fused))
    return history


def main():
    for name, h, c, v, s in [
        ("clean-dry", 0.3, 0.2, 5, 1.0),
        ("dirty-humid", 0.9, 1.2, 5, 0.5),
    ]:
        print(name)
        for step, length, bridged, fused in growth(h, c, v, s):
            flag = "FUSE" if fused else ("BRIDGE" if bridged else "")
            print(f"  {step:2d} dendrite={length:.3f} {flag}")
    print("Invented growth law; demonstrates bridge/fuse/regrow behavior only.")


if __name__ == "__main__":
    main()
