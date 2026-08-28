"""Compare synthetic perimeter wire-bond and area-array interconnect capacity."""

def perimeter_sites(side_mm: float, pitch_mm: float) -> int:
    return int((4 * side_mm) // pitch_mm)


def area_sites(side_mm: float, pitch_mm: float) -> int:
    n = int(side_mm // pitch_mm)
    return n * n


def main() -> None:
    side = 10.0
    print(f"Synthetic {side:.1f} mm square die")
    for pitch in [1.0, 0.5, 0.25]:
        print(
            f"pitch={pitch:4.2f} mm  perimeter~{perimeter_sites(side, pitch):4d}  area-array~{area_sites(side, pitch):5d}"
        )


if __name__ == "__main__":
    main()
