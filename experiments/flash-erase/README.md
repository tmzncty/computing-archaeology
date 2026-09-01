# Flash erase granularity

## Historical question

What system work appears when a nonvolatile array can program small units but must erase a larger group before those cells can be reused?

## Run

```bash
python experiments/flash-erase/flash_erase.py
```

## Model

A deterministic synthetic array has eight blocks of eight pages. One hundred twenty-eight updates target one logical page. The `in_place` strategy erases the containing block on every update. The `append_reclaim` strategy writes successive versions into free physical pages and only reclaims a block after cycling through the available array.

## What it demonstrates

- small logical updates need not map to equally small physical erases;
- out-of-place updates can postpone erase work;
- erase placement changes how concentrated wear becomes;
- hiding erase granularity requires mapping state and reclamation policy below a block interface.

## What it cannot establish

This is not a NAND command-set emulator, flash-translation layer, endurance predictor, or performance benchmark. It omits invalid-page accounting, garbage-collection copying, bad blocks, ECC, retention, program/erase timing, overprovisioning, and power-loss recovery. Its geometry and counts are invented to make one constraint visible.
