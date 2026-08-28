"""Synthetic inspection workload model.

Not calibrated to a real AOI, ICT, or X-ray system.
"""


def evaluate(units=1_000_000, defect_rate=0.002, detection=0.95, false_call=0.001):
    defects = units * defect_rate
    good = units - defects
    caught = defects * detection
    escaped = defects - caught
    false_reviews = good * false_call
    total_reviews = caught + false_reviews
    print(f"units={units}")
    print(f"true_defects={defects:.0f}")
    print(f"caught={caught:.0f}")
    print(f"escaped={escaped:.0f}")
    print(f"false_reviews={false_reviews:.0f}")
    print(f"review_load={total_reviews:.0f}")


if __name__ == "__main__":
    evaluate()
