# Why HBM4 Made the Memory Interface Even Wider

HBM's basic trick is to stop asking a few pins to run impossibly fast and instead use a very wide, very short interface beside the accelerator.

## Historical record

Micron describes HBM4 with a 2048-pin data interface and more than 2.8 TB/s per stack in its current product material. SK hynix announced completion and mass-production readiness of HBM4 in September 2025, emphasizing roughly doubled bandwidth over the prior generation.[^micron][^sk]

## Engineering reconstruction

Bandwidth can be increased by more transfers per pin, more pins, or both.

HBM4 pushes the width dimension aggressively:

```text
many DRAM dies
  -> TSV stack
  -> wide base-die interface
  -> package/interposer
  -> accelerator
```

The wider interface reduces the distance each bit must travel, but increases base-die complexity, package routing, bump/bond count, power delivery, test coverage, and yield coupling.

## Speed connection

Accelerator FLOPS are wasted whenever arithmetic waits for weights, activations, or KV-cache data. Memory bandwidth therefore becomes compute utilization.

## Experiment

`experiments/hbm4-interface/hbm4_interface.py` compares synthetic interface width, per-pin rate, aggregate bandwidth, and interconnect-power proxy.

[^micron]: Micron, “HBM4,” https://www.micron.com/products/memory/hbm/hbm4
[^sk]: SK hynix, “Completes World's First HBM4 Development and Readies Mass Production,” 2025, https://news.skhynix.com/en/sk-hynix-completes-worlds-first-hbm4-development-and-readies-mass-production/
