"""Synthetic interconnect liner/barrier geometry model."""


def remaining_area(width, height, liner):
    inner_w = max(0.0, width - 2 * liner)
    inner_h = max(0.0, height - 2 * liner)
    total = width * height
    conductor = inner_w * inner_h
    return conductor, conductor / total if total else 0.0


def main():
    print("fixed liner thickness = 2 synthetic units")
    for size in (40, 24, 16, 12, 8, 6):
        area, frac = remaining_area(size, size, 2)
        print(f"feature={size:2d}x{size:2d} conductor_area={area:6.1f} conductor_fraction={frac:5.3f}")


if __name__ == "__main__":
    main()
