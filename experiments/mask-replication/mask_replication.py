"""Synthetic systematic-vs-random defect model."""

import random

DIE = 100
RANDOM_FAIL_PROB = 0.03
random.seed(7)

random_failures = sum(random.random() < RANDOM_FAIL_PROB for _ in range(DIE))
print(f"Independent random failures: {random_failures}/{DIE}")

mask_defect_present = True
systematic_failures = DIE if mask_defect_present else 0
print(f"Replicated mask defect failures: {systematic_failures}/{DIE}")
print("A reusable pattern amplifies both precision and systematic error.")