"""Compare synthetic perimeter wire-bond and area-array interconnect capacity."""

from fractions import Fraction


def _positive_decimal_measurement(value: float, name: str) -> Fraction:
    """Return one finite, positive measurement without binary-float drift."""
    message = f"{name} must be finite and strictly positive"
    try:
        measurement = Fraction(str(value))
    except (ValueError, ZeroDivisionError) as error:
        raise ValueError(message) from error
    if measurement <= 0:
        raise ValueError(message)
    return measurement


def perimeter_sites(side_mm: float, pitch_mm: float) -> int:
    side = _positive_decimal_measurement(side_mm, "side_mm")
    pitch = _positive_decimal_measurement(pitch_mm, "pitch_mm")
    return (4 * side) // pitch


def area_sites(side_mm: float, pitch_mm: float) -> int:
    side = _positive_decimal_measurement(side_mm, "side_mm")
    pitch = _positive_decimal_measurement(pitch_mm, "pitch_mm")
    n = side // pitch
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
