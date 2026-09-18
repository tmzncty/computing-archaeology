#!/usr/bin/env python3
"""Compare an ideal circle with an inscribed regular polygon on a point-sampled raster.

This is a synthetic engineering experiment, not a historical emulator.
"""

from __future__ import annotations

import argparse
import math


def polygon_metrics(n: int, radius: float = 1.0) -> tuple[float, float, float]:
    if n < 3:
        raise ValueError("n must be at least 3")
    side = 2.0 * radius * math.sin(math.pi / n)
    sagitta = radius * (1.0 - math.cos(math.pi / n))
    half_pixel_radius = math.inf if sagitta == 0 else 0.5 * radius / sagitta
    return side, sagitta, half_pixel_radius


def polygon_radial_boundary(theta: float, n: int, radius: float) -> float:
    """Return radius of an inscribed regular n-gon boundary in direction theta.

    Vertices are at angles 2*pi*k/n. Side normals lie halfway between adjacent
    vertices.
    """
    sector = 2.0 * math.pi / n
    delta = (theta % sector) - sector / 2.0
    inradius = radius * math.cos(math.pi / n)
    return inradius / math.cos(delta)


def scan(radius: int, n: int) -> tuple[int, int, int]:
    """Point-sample pixel centers and compare inside/outside classifications."""
    if radius < 1:
        raise ValueError("radius must be positive")

    pad = 2
    limit = radius + pad
    circle_only = 0
    polygon_only = 0
    same = 0
    r2 = float(radius * radius)

    for iy in range(-limit, limit + 1):
        y = iy + 0.5
        for ix in range(-limit, limit + 1):
            x = ix + 0.5
            d2 = x * x + y * y
            inside_circle = d2 <= r2

            if d2 == 0.0:
                inside_polygon = True
            else:
                theta = math.atan2(y, x)
                boundary = polygon_radial_boundary(theta, n, float(radius))
                inside_polygon = d2 <= boundary * boundary

            if inside_circle == inside_polygon:
                same += 1
            elif inside_circle:
                circle_only += 1
            else:
                polygon_only += 1

    return same, circle_only, polygon_only


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=65537, help="number of polygon sides")
    parser.add_argument("--radius", type=int, default=512, help="raster circumradius in pixels")
    parser.add_argument("--scan", action="store_true", help="run point-sampled raster comparison")
    args = parser.parse_args()

    side, sagitta, half_pixel_radius = polygon_metrics(args.n)

    print(f"n = {args.n}")
    print(f"unit-radius side length = {side:.15g}")
    print(f"unit-radius maximum radial gap = {sagitta:.15g}")
    print(f"radius for 0.5-pixel maximum gap = {half_pixel_radius:.15g} px")
    print(
        f"at radius {args.radius}px, maximum radial gap = "
        f"{args.radius * sagitta:.15g} px"
    )

    if args.scan:
        same, circle_only, polygon_only = scan(args.radius, args.n)
        total = same + circle_only + polygon_only
        print()
        print("point-sampled raster comparison")
        print(f"sampled pixels = {total}")
        print(f"same classification = {same}")
        print(f"circle-only samples = {circle_only}")
        print(f"polygon-only samples = {polygon_only}")


if __name__ == "__main__":
    main()
