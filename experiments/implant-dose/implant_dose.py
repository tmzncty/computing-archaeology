"""Conceptual implant dose / activation model. Synthetic parameters only."""

def active_dopant(dose: float, activation: float) -> float:
    return dose * activation


def main() -> None:
    doses = [1e11, 1e12, 1e13, 1e14]
    activations = [0.5, 0.8, 0.95]
    print("Synthetic ion-implant activation model")
    for a in activations:
        print(f"activation={a:.0%}")
        for d in doses:
            print(f"  dose={d:.1e} -> active={active_dopant(d, a):.2e}")


if __name__ == "__main__":
    main()
