"""Synthetic PCB surface-finish decision model."""

FINISHES = {
    "OSP": dict(cost=9, flatness=10, storage=5, bond=2, process_risk=6),
    "ENIG": dict(cost=5, flatness=9, storage=8, bond=6, process_risk=5),
    "NiAu": dict(cost=2, flatness=7, storage=9, bond=10, process_risk=7),
    "ImmAg": dict(cost=6, flatness=9, storage=6, bond=4, process_risk=6),
}


def score(v, weights):
    return sum(v[k] * weights[k] for k in weights)


def main():
    scenarios = {
        "consumer-smt": dict(cost=3, flatness=3, storage=1, bond=0, process_risk=-1),
        "wire-bond": dict(cost=1, flatness=2, storage=1, bond=4, process_risk=-1),
        "long-storage": dict(cost=1, flatness=1, storage=4, bond=0, process_risk=-1),
    }
    for scenario, weights in scenarios.items():
        ranked = sorted(((score(v, weights), k) for k, v in FINISHES.items()), reverse=True)
        print(scenario, "->", ", ".join(f"{name}:{value}" for value, name in ranked))


if __name__ == "__main__":
    main()
