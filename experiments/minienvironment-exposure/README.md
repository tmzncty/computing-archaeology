# Minienvironment Exposure

A synthetic contamination-budget model for open versus podded wafer handling.

Run:

```bash
python experiments/minienvironment-exposure/minienvironment_exposure.py
```

The script multiplies an invented particle-exposure rate by exposed time and area. It is not a cleanroom or SMIF contamination model.

It exists to make the logic in [`../../docs/manufacturing/why-smif-put-the-cleanroom-around-the-wafer.md`](../../docs/manufacturing/why-smif-put-the-cleanroom-around-the-wafer.md) visible: reducing how long and how directly the product sees the general room can be more powerful than trying to make every cubic meter of the factory equally clean.