# Finite Differences Experiment

Historical question:

> Why is the method of finite differences attractive when addition is easier to implement mechanically than multiplication or division?

This tiny experiment is intentionally not a Babbage emulator. It isolates one design pressure.

## What it does

`finite_difference.py` compares two ways of generating values of a polynomial at successive integer inputs:

1. direct evaluation of the polynomial;
2. a finite-difference table that advances using addition after initialization.

The program counts abstract arithmetic operations so that the user can apply different synthetic cost models.

## Why this is historically relevant

The Computer History Museum's Babbage material explains that finite differences let a difference engine calculate polynomial tables using addition rather than requiring mechanical multiplication and division.

Source:

- Computer History Museum, “How it Works,” https://www.computerhistory.org/babbage/howitworks/

## What this experiment does **not** prove

It does not model:

- Babbage's exact mechanisms;
- gear backlash;
- carry timing;
- decimal-wheel geometry;
- manufacturing tolerances;
- the printer;
- human setup labor;
- the full cost of Difference Engine No. 1 or No. 2.

It demonstrates only the algorithmic transformation that makes repeated addition possible.

## Run

```bash
python experiments/finite-differences/finite_difference.py
```

No third-party dependencies are required.

## Try changing the cost model

The script prints a simple weighted cost estimate. Edit:

```python
COST_ADD = 1
COST_MUL = 10
```

Then ask:

- At what multiplication/addition cost ratio does the finite-difference method become attractive?
- What changes for higher-degree polynomials?
- What if carries are expensive?
- What if initialization cost matters because you only need a few values?

That last question is important: engineering tradeoffs depend on workload, not merely on operation type.
