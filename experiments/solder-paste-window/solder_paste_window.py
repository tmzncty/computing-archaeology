"""Synthetic solder-paste print/reflow tradeoff model."""


def print_score(aperture, particle, rheology=0.9):
    ratio = aperture / particle
    geometry = min(1.0, max(0.0, (ratio - 2.0) / 4.0))
    return geometry * rheology


def oxide_burden(particle):
    # Smaller particles -> more surface per metal volume, synthetic inverse proxy.
    return 1.0 / particle


def joint_score(printing, flux_activity, burden):
    cleaning = min(1.0, flux_activity / (0.5 + burden))
    residue_penalty = max(0.0, flux_activity - 1.2) * 0.15
    return max(0.0, printing * cleaning - residue_penalty)


def main():
    aperture = 30.0
    for particle in (12.0, 8.0, 6.0, 4.0):
        p = print_score(aperture, particle)
        burden = oxide_burden(particle) * 4.0
        score = joint_score(p, 1.0, burden)
        print(
            f"particle={particle:4.1f} print={p:5.3f} "
            f"oxide_proxy={burden:5.3f} joint_proxy={score:5.3f}"
        )


if __name__ == "__main__":
    main()
