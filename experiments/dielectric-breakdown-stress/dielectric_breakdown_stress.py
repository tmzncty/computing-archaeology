"""Synthetic TDDB stress model. Not a lifetime predictor."""

import math


def life_proxy(field, temperature_c, area):
    field_factor = math.exp(-0.55 * (field - 5.0))
    temp_factor = math.exp(-0.018 * (temperature_c - 50.0))
    area_factor = 1.0 / area
    return field_factor * temp_factor * area_factor


def main():
    print("Synthetic TDDB relative-life proxy")
    for field, temp, area in [(5, 50, 1), (7, 50, 1), (7, 100, 1), (7, 100, 10)]:
        print(
            f"field={field:.1f} temp={temp:3.0f}C area={area:2.0f} "
            f"relative_life={life_proxy(field, temp, area):.6f}"
        )
    print("All coefficients are invented teaching values.")


if __name__ == "__main__":
    main()
