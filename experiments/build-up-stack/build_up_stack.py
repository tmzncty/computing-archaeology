"""Synthetic package build-up stack model.

Not calibrated to ABF, BT resin, any substrate vendor, or any real package.
"""


def stack_metrics(layers, layer_survival=0.992, vias_per_layer=1200):
    routing_proxy = layers * 1.0
    stack_survival = layer_survival ** layers
    via_burden = layers * vias_per_layer
    return routing_proxy, stack_survival, via_burden


def main():
    for layers in [2, 4, 6, 8, 12]:
        routing, survival, vias = stack_metrics(layers)
        print(
            f"layers={layers:2d} routing_proxy={routing:4.1f} "
            f"stack_survival={survival:.4f} via_burden={vias}"
        )


if __name__ == "__main__":
    main()
