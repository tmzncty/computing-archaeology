"""Synthetic ALD-like saturation/purge window model."""

import math


def coverage(dose):
    return 1.0 - math.exp(-dose)


def impurity(purge):
    return math.exp(-purge)


def main():
    for dose, purge in [(0.4, 0.5), (1.0, 1.0), (2.0, 2.0), (4.0, 4.0)]:
        cov = coverage(dose)
        imp = impurity(purge)
        quality = cov * (1.0 - imp)
        print(f"dose={dose:3.1f} purge={purge:3.1f} coverage={cov:6.3f} residual={imp:6.3f} quality_proxy={quality:6.3f}")


if __name__ == "__main__":
    main()
