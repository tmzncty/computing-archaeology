"""Synthetic burn-in / screening tradeoff model.

Not a reliability model for any real semiconductor family.
"""

from dataclasses import dataclass


@dataclass
class Case:
    name: str
    weak_removed: float
    good_damage: float
    screening_cost: float


def evaluate(population=10000, latent_weak_fraction=0.04):
    cases = [
        Case("none", 0.00, 0.000, 0.0),
        Case("moderate", 0.70, 0.002, 1.0),
        Case("aggressive", 0.95, 0.010, 2.5),
    ]
    weak = population * latent_weak_fraction
    good = population - weak
    for case in cases:
        weak_shipped = weak * (1 - case.weak_removed)
        good_lost = good * case.good_damage
        shipped = population - weak * case.weak_removed - good_lost
        early_failure_fraction = weak_shipped / shipped
        print(
            f"{case.name:10s} shipped={shipped:8.0f} "
            f"weak_shipped={weak_shipped:6.0f} "
            f"early_risk={early_failure_fraction:7.4%} "
            f"screen_cost={case.screening_cost:3.1f}"
        )


if __name__ == "__main__":
    evaluate()
