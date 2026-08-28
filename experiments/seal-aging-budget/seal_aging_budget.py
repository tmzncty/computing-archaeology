"""Synthetic vacuum-seal aging budget.

Not a lifetime model for any real elastomer.
"""


def damage(temp_cycles, plasma_hours, door_cycles):
    return temp_cycles * 0.8 + plasma_hours * 1.4 + door_cycles * 0.02


def main():
    cases = [
        ("light", 20, 10, 200),
        ("thermal-heavy", 80, 10, 200),
        ("plasma-heavy", 20, 80, 200),
        ("motion-heavy", 20, 10, 3000),
    ]
    threshold = 100
    for name, t, p, d in cases:
        score = damage(t, p, d)
        print(f"{name:14s} damage={score:7.2f} threshold={threshold} replace={score >= threshold}")


if __name__ == "__main__":
    main()
