"""Synthetic effective-width versus stack-burden model."""

for sheets in (1, 2, 3, 4):
    for width in (1.0, 1.5, 2.0):
        effective_width = sheets * width
        process_burden = 1.0 + 0.22 * (sheets - 1) + 0.08 * (width - 1.0)
        score = effective_width / process_burden
        print(f"sheets={sheets} width={width:.1f} Weff={effective_width:.2f} burden={process_burden:.2f} score={score:.2f}")
