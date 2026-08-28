"""Synthetic microvia conformal versus bottom-up fill model."""


def fill(depth=8, cycles=6, bottom_bias=0.0):
    cells = [0.0] * depth
    for _ in range(cycles):
        for i in range(depth):
            cells[i] += 1.0 + bottom_bias * (i / max(depth - 1, 1))
    throat = cells[0]
    bottom = cells[-1]
    void_proxy = max(throat - bottom, 0.0)
    return throat, bottom, void_proxy


def main():
    for name, bias in [("conformal", 0.0), ("bottom-up", 0.8), ("strong-bottom-up", 1.5)]:
        throat, bottom, void = fill(bottom_bias=bias)
        print(f"{name:16s} throat={throat:6.2f} bottom={bottom:6.2f} void_proxy={void:6.2f}")


if __name__ == "__main__":
    main()
