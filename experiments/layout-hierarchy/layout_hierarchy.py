"""Toy hierarchy-versus-flat layout representation model.

Not a GDSII parser or file-size estimator.
"""


def compare(cell_shapes=12, rows=64, cols=64, reference_cost=1):
    instances = rows * cols
    flat_shapes = cell_shapes * instances
    hierarchical_units = cell_shapes + instances * reference_cost
    print(f"cell_shapes={cell_shapes}")
    print(f"instances={instances}")
    print(f"flat_shape_units={flat_shapes}")
    print(f"hierarchical_units={hierarchical_units}")
    print(f"ratio={flat_shapes / hierarchical_units:0.2f}x")


if __name__ == "__main__":
    compare()
