"""Synthetic channel-loss budget with and without regeneration."""

paths = [
    ("short", 18, None),
    ("long-passive", 42, None),
    ("long-retimed", 42, 22),
]
limit = 30
for name, total_loss, split in paths:
    if split is None:
        pass_link = total_loss <= limit
        burden = 1.0
    else:
        second = total_loss - split
        pass_link = split <= limit and second <= limit
        burden = 1.25
    print(f"{name:13s} total_loss={total_loss:2d} split={str(split):>4s} pass={pass_link} active_burden={burden:.2f}")
