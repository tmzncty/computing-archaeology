"""Synthetic board-density comparison for through-hole vs surface mount."""

COMPONENTS = 100
BODY_AREA = 20.0
TH_KEEP_OUT_PER_LEAD = 4.0
SMT_PAD_KEEP_OUT_PER_LEAD = 1.2
LEADS = 14

through_hole = COMPONENTS * (BODY_AREA + LEADS * TH_KEEP_OUT_PER_LEAD)
smt = COMPONENTS * (BODY_AREA + LEADS * SMT_PAD_KEEP_OUT_PER_LEAD)

print(f"through-hole synthetic occupied/routing pressure area: {through_hole:.1f}")
print(f"surface-mount synthetic occupied/routing pressure area: {smt:.1f}")
print(f"relative SMT footprint pressure: {smt/through_hole:.2%}")