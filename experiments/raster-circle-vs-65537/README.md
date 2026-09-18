# Raster Circle vs. Regular 65,537-gon

Historical/engineering question:

> When two geometric objects are distinct in continuous mathematics, how much of that distinction survives a finite raster display?

This experiment accompanies [the 65,537-gon case study](../../case-studies/regular-65537-gon/from-constructibility-to-pixels.md).

## What it does

compare.py reports:

- the side length of an inscribed regular n-gon for unit circumradius;
- the maximum radial gap between the polygon and its circumcircle;
- the radius, measured in pixels, at which that gap reaches half a pixel;
- optionally, a point-sampled raster comparison between a circle and an inscribed regular polygon.

The default is n=65537.

## Why this is useful

The regular 65,537-gon is mathematically not a circle. But finite rasterization is a many-to-one representation: distinct source geometries can map to the same sampled pixels.

For n=65537,

\[
1-\cos(\pi/n)\approx1.15\times10^{-9}.
\]

A half-pixel radial difference therefore appears only at a circumradius of roughly \(4.35\times10^8\) pixels under this simple geometric criterion.

## Run

Summary only:

    python experiments/raster-circle-vs-65537/compare.py

Also compare point-sampled pixels at a practical radius:

    python experiments/raster-circle-vs-65537/compare.py --scan --radius 512

Try a smaller polygon to make the distinction visible:

    python experiments/raster-circle-vs-65537/compare.py --n 64 --scan --radius 256

## Model

The raster scan treats each pixel as one sample at its center.

For the circle, a sample is inside when

\[
x^2+y^2\le R^2.
\]

For the regular polygon, the program uses the analytic radial boundary of an inscribed regular polygon.

## What this experiment does **not** prove

It does not model:

- antialiasing or multisample coverage;
- line/stroke width;
- Bézier or GPU tessellation rules;
- subpixel layout;
- gamma and color response;
- pixel aperture shape;
- human visual acuity;
- a particular historical display controller;
- the rendering implementation used by Manim.

A zero difference count means only that **this point-sampling model** produced the same classifications at that resolution and alignment.

The experiment demonstrates representational collapse under finite sampling. It does not show that every renderer must produce identical images.
