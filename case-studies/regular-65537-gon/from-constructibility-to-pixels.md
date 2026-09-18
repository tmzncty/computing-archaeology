# From Constructibility to Pixels: the Regular 65,537-gon

## Question

What happens when an exact object from classical geometry is turned into a computer artifact and finally shown on a raster display?

The regular 65,537-gon is an unusually sharp case because the mathematical object, the construction procedure, the numerical execution, the rendered animation, and the final pixels are all different representations of "the same" result.

## Historical record

A regular polygon is straightedge-and-compass constructible exactly when its number of sides has the Gauss-Wantzel form: a power of two multiplied by distinct Fermat primes. Since

\[
65537 = 2^{2^4}+1
\]

is a Fermat prime, the regular 65,537-gon is constructible.[^eom-geometric-constructions]

Johann Gustav Hermes announced a complete construction in 1894 after roughly ten years of work. The construction became famous partly because of its scale; surviving manuscript material is associated with Göttingen.[^mathworld-65537]

In 2026, the open-source project ofoa/regular-65537-gon turned this problem into an executable construction pipeline. Its published artifact constructs the target point

\[
(\cos(2\pi/65537),\sin(2\pi/65537))
\]

from straightedge-and-compass primitives. The repository reports 20,680 drawing steps: 19,206 circles and 1,474 lines, with 20,034 geometric intersections and 723 quadratic splits. It re-executes the geometry at 180- and 240-decimal-digit precision, while explicitly stating that this is numerical validation rather than a formal proof and that 20,680 is not claimed to be minimal.[^ofoa-readme]

The project follows a modern treatment by J. Mainik, whose 2025 paper gives a detailed construction of the 65,537-gon and discusses the earlier Hermes work.[^mainik]

## Engineering reconstruction: where "exactness" moves

The useful computing-archaeology point is not simply that the polygon is large. It is that exactness changes meaning as the object moves through layers.

1. **Abstract geometry.** A circle and a regular 65,537-gon are distinct mathematical objects. The circle has continuous curvature; the polygon consists of 65,537 straight sides.
2. **Symbolic construction.** The target point can be described through field operations and nested quadratic extensions.
3. **Executable geometry.** Those operations can be compiled into straightedge-and-compass primitives and intersection choices.
4. **Finite-precision verification.** A computer replays the construction with high-precision arithmetic and checks that the resulting values agree with the intended algebraic quantities.
5. **Graphics scene.** A renderer turns geometric primitives into a scene with coordinates, line widths, camera transforms, timing, and labels.
6. **Raster image.** The scene is sampled onto a finite grid of pixels.
7. **Physical display.** Pixels are emitted by finite-sized subpixels with their own optical behavior.

At the first layer, "circle" and "65,537-gon" are rigorously different. At the sixth layer, they may map to exactly the same finite pixel pattern.

That is not a paradox. The display is not the mathematical object; it is a finite representation of it.

## How close is the polygon to its circumcircle?

For an inscribed regular \(n\)-gon of circumradius \(R\), the largest radial gap between a side and the circle occurs at the midpoint of a side:

\[
\Delta = R\left(1-\cos\frac{\pi}{n}\right).
\]

For \(n=65537\),

\[
1-\cos\frac{\pi}{65537}
\approx 1.14894\times10^{-9}.
\]

So if the circumradius on screen is \(R\) pixels, the maximum geometric deviation is only

\[
\Delta_{\rm px}\approx 1.14894\times10^{-9}R.
\]

A half-pixel deviation is not reached until the radius is roughly

\[
R\approx\frac{0.5}{1-\cos(\pi/65537)}
\approx 4.35\times10^8\text{ pixels}.
\]

This number should **not** be treated as a universal perceptual threshold. Antialiasing, stroke width, subpixel coverage, floating-point implementation, camera alignment, and display optics can all change what becomes visible. It is instead an order-of-magnitude demonstration of how quickly a very high-order polygon collapses into the same raster representation as a circle.

The unit-circle side length is still nonzero:

\[
2\sin\frac{\pi}{65537}\approx9.58723\times10^{-5},
\]

but a renderer does not preserve that distinction merely because the distinction exists mathematically.

## Why the computer's "circle" is also not the mathematical circle

On a raster display, a circle is normally represented by a finite set of pixel samples or pixel-coverage values. Those samples are neither the continuum

\[
x^2+y^2=R^2
\]

nor necessarily a polygon in the strict mathematical sense. They are a discrete image of a geometric primitive.

A vector graphics API may keep a circle, ellipse, Bézier path, or tessellated approximation in a higher-level representation for some portion of the pipeline, but the ordinary screen output still ends at a finite raster.

This is the important distinction:

> a regular 65,537-gon is not a circle, while a rasterized picture of either object is not the original geometric object at all.

The final image can therefore erase a distinction that remains perfectly meaningful in the source geometry.

## Why this belongs in computing archaeology

This case exposes a recurring property of computing systems: **representation boundaries can hide distinctions that exist at another layer.**

The same pattern appears elsewhere:

- analog values become quantized digital samples;
- continuous time becomes clocked state transitions;
- real-valued coordinates become integer or fixed-point device coordinates;
- vector descriptions become raster coverage;
- source-level structure disappears into machine code;
- high-precision internal calculations are reduced to finite output formats.

The 65,537-gon is useful because all of these questions become visible in one artifact. The mathematics says the object can be constructed exactly in the classical sense. The software encodes a long explicit procedure. High-precision replay validates numerical consistency. The video then compresses all of that structure into pixels that may no longer reveal whether the source was a circle or a 65,537-sided polygon.

For preservation, this also matters: the **RCG instruction file, source code, validation reports, and mathematical derivation contain evidence that the rendered video does not**. A video frame alone is not enough to recover the construction.

## Experiment

See [the raster-circle-vs-65537 experiment](../../experiments/raster-circle-vs-65537/) for a small synthetic experiment that compares the circle/polygon deviation with pixel scale and can point-sample both shapes on a finite raster.

The experiment is an engineering model. It is not evidence about the historical intent of Gauss, Hermes, Mainik, or the 2026 project author.

## Sources

[^eom-geometric-constructions]: Encyclopedia of Mathematics, “Geometric constructions,” https://encyclopediaofmath.org/wiki/Geometric_constructions

[^mathworld-65537]: Eric W. Weisstein, “65537-gon,” *MathWorld*, https://mathworld.wolfram.com/65537-gon.html

[^ofoa-readme]: ofoa, “正65537边形：20,680步尺规作图,” ofoa/regular-65537-gon, GitHub, https://github.com/ofoa/regular-65537-gon

[^mainik]: J. Mainik, “Regular polygons,” arXiv:2505.14865, 2025, https://arxiv.org/abs/2505.14865
