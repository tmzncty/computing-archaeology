# Why HBM Moved Memory Beside the Processor

A fast processor can spend much of its time waiting on memory bandwidth. One response was not simply to clock conventional board memory faster, but to move many memory wires physically closer to the compute die.

## Historical record

SK hynix describes beginning HBM development in 2009 around TSV and wafer-level packaging, introducing early TSV-based HBM in 2013/2014, and collaborating with AMD on first-generation HBM products.[^skhynix]

AMD's 2015 Radeon R9 Fury announcement described a 4096-bit HBM interface and emphasized bandwidth and PCB-area advantages over GDDR5.[^amd]

## Engineering reconstruction

Conventional external memory trades package pins, PCB traces, signaling energy, and frequency against bandwidth.

HBM changes the geometry:

```text
DRAM die
DRAM die
DRAM die
DRAM die
  || TSVs
base / logic interface
======== interposer ======== GPU / accelerator
```

Instead of a relatively narrow very-high-speed off-package channel, HBM uses an extremely wide nearby interface.

## New dependencies

Bandwidth moves into packaging:

- TSV formation and yield;
- wafer thinning;
- die stacking;
- microbump/bond alignment;
- known-good-die strategy;
- interposer routing;
- package warpage;
- thermal path through a stack;
- memory/logic co-design.

Memory architecture becomes packaging architecture.

## Experiment

[`experiments/hbm-bandwidth-density/hbm_bandwidth_density.py`](../../experiments/hbm-bandwidth-density/hbm_bandwidth_density.py) compares synthetic narrow/high-rate and wide/lower-rate interfaces while charging a board-area/interconnect-energy proxy.

## Source caution

SK hynix and AMD sources are corporate histories and product announcements. Their priority language should be treated as company claims and cross-checked for formal standards history.

[^skhynix]: SK hynix, “Continuing to Make HBM History,” https://news.skhynix.com/en/the-story-of-sk-hynixs-hbm-development/
[^amd]: AMD, Radeon R9 Fury/HBM announcement, 2015, https://ir.amd.com/news-events/press-releases/detail/619/amd-ushers-in-a-new-era-of-pc-gaming-with-radeontm-r9-and-r7-300-series-graphics-line-up-including-worlds-first-graphics-family-with-revolutionary-hbm-technology
