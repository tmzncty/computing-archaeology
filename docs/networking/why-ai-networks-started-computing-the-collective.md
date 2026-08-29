# Why AI Networks Started Computing the Collective

When thousands of accelerators repeatedly perform reductions, the network can spend enormous bandwidth moving partial results that are immediately combined.

## Historical record

NVIDIA describes SHARP as offloading collective operations such as reductions into aggregation nodes, reducing repeated endpoint traffic and freeing CPU/GPU resources. NVLink SHARP similarly allows supported NCCL collectives to be offloaded into the NVSwitch domain.[^sharp][^nvls]

## Engineering reconstruction

Traditional reduction:

```text
GPU -> network -> GPU/CPU combines
    -> network -> more combining
```

In-network reduction:

```text
GPU -> switch/aggregation node combines
    -> smaller reduced data continues
```

The network stops being only a transporter and becomes an arithmetic participant.

## Speed connection

Large-model training and inference are often limited by collective latency and bandwidth. Offloading reduction can shorten critical communication phases and leave accelerators doing useful compute instead of protocol work.

## Experiment

`experiments/collective-offload/collective_offload.py` compares synthetic bytes moved and endpoint work for endpoint-only versus tree/in-network reduction.

[^sharp]: NVIDIA, “SHARP Introduction,” https://networking-docs.nvidia.com/sharpum/3150/introduction
[^nvls]: NVIDIA NCCL documentation, `NCCL_NVLS_ENABLE`, https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html
