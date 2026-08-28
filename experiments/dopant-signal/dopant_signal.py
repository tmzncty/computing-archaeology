"""Synthetic purity-vs-doping model. Not a historical fab reconstruction."""

SCENARIOS = [
    (1e16, 1e15),
    (1e16, 1e13),
    (1e16, 1e11),
    (1e16, 1e9),
]

print("intended_dopant  background  signal/background")
for dopant, background in SCENARIOS:
    ratio = dopant / background
    print(f"{dopant:14.2e}  {background:10.2e}  {ratio:17.2e}")

print("\nInterpretation: lower uncontrolled background gives intentional doping more authority over device behavior.")