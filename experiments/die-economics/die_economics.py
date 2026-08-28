import math

WAFER_AREA_MM2 = math.pi * (100 / 2) ** 2  # synthetic 100 mm wafer
EDGE_LOSS = 0.15
DEFECT_DENSITY = 0.004  # synthetic defects/mm^2
WAFER_COST = 220.0      # synthetic dollars
PACKAGE_TEST = 1.20     # synthetic dollars per good die


def estimate(die_area):
    usable_area = WAFER_AREA_MM2 * (1 - EDGE_LOSS)
    gross_die = usable_area / die_area
    yield_fraction = math.exp(-DEFECT_DENSITY * die_area)
    good_die = gross_die * yield_fraction
    silicon_cost = WAFER_COST / good_die
    total_cost = silicon_cost + PACKAGE_TEST
    return gross_die, yield_fraction, good_die, total_cost


def main():
    print("Synthetic die-economics model")
    print("area mm^2 | gross die | yield  | good die | cost/good")
    print("----------+-----------+--------+----------+----------")
    for area in [15, 20, 25, 30, 40, 50, 70]:
        gross, yld, good, cost = estimate(area)
        print(f"{area:9.0f} | {gross:9.1f} | {yld:6.1%} | {good:8.1f} | ${cost:7.2f}")

    print("\nAll wafer/process/cost numbers are invented teaching parameters.")
    print("The model shows why die area can constrain product economics; it is not MOS fab data.")


if __name__ == "__main__":
    main()
