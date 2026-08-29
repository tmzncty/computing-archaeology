# Why Silicon Interposers Became System-Scale Wiring

Once compute and HBM became separate high-density dies, ordinary package substrate routing was no longer the only useful wiring scale.

The silicon interposer created an intermediate wiring world between on-die metal and motherboard traces.

## Historical record

TSMC states that CoWoS has been in production since 2012 and describes CoWoS-S silicon interposers carrying logic chiplets and HBM, with later generations expanding to multiple-reticle-scale interposer areas.[^cowos]

## Engineering reconstruction

An interposer changes distance and density:

```text
HBM     logic     HBM
 |        |        |
 +--------+--------+
   silicon interposer
 ====================
 package substrate
 ====================
 motherboard
```

The interposer can provide much denser wiring than the motherboard while covering a much larger area than one logic die.

## Reticle limits become architecture

A monolithic die is constrained by lithographic field size, defect yield, and cost. An interposer permits multiple dies to communicate across a package-level fabric.

That does not abolish limits. It creates new ones:

- interposer size and yield;
- TSVs through the interposer;
- microbump pitch;
- power delivery across a large package;
- warpage;
- package substrate escape routing;
- test and repair strategy;
- thermal gradients.

## Experiment

[`experiments/interposer-reach/interposer_reach.py`](../../experiments/interposer-reach/interposer_reach.py) compares synthetic board-scale and interposer-scale wiring density/reach, then adds package-area and yield burden.

## Source caution

TSMC's chronology is authoritative for TSMC's CoWoS platform, but it is not a neutral history of all silicon-interposer work.

[^cowos]: TSMC, “CoWoS,” https://3dfabric.tsmc.com/english/dedicatedFoundry/technology/cowos.htm
