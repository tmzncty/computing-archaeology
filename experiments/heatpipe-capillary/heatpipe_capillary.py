"""Synthetic heat-pipe transport-limit model. Not a thermal design calculator."""


def capacity(wick, distance, orientation, condenser):
    capillary = wick * orientation / max(distance, 0.1)
    return min(capillary, condenser)


def main():
    cases = [
        ("short level", 120, 1.0, 1.0, 100),
        ("long level", 120, 2.0, 1.0, 100),
        ("long adverse", 120, 2.0, 0.55, 100),
        ("strong wick weak condenser", 200, 1.0, 1.0, 65),
    ]
    for name, wick, dist, orient, condenser in cases:
        c = capacity(wick, dist, orient, condenser)
        print(f"{name:26s} synthetic_capacity={c:7.2f}")
    print("All values are invented teaching parameters; real heat pipes have multiple limits.")


if __name__ == "__main__":
    main()
