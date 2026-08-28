"""Synthetic process drift / measurement / hold model.

This is a teaching model, not historical fab data.
"""

from dataclasses import dataclass


@dataclass
class Run:
    step: int
    value: float
    measured: bool
    held: bool


def simulate(
    steps: int = 30,
    start: float = 0.0,
    drift_per_step: float = 0.08,
    measure_every: int = 5,
    control_limit: float = 0.55,
):
    value = start
    held = False
    output = []
    for step in range(1, steps + 1):
        if not held:
            value += drift_per_step
        measured = step % measure_every == 0
        if measured and abs(value) > control_limit:
            held = True
        output.append(Run(step, value, measured, held))
    return output


def main():
    runs = simulate()
    for run in runs:
        flag = "MEASURE" if run.measured else ""
        state = "HOLD" if run.held else "RUN"
        print(f"{run.step:02d} value={run.value:0.2f} {flag:7s} {state}")


if __name__ == "__main__":
    main()
