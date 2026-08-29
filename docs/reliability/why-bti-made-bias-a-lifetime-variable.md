# Why BTI Made Bias a Lifetime Variable

A transistor does not have to be switching to age.

That is the historical importance of **bias-temperature instability** (BTI).

## Historical record

Negative bias temperature instability (NBTI) was reported in MOS devices decades before it became one of the dominant scaled-CMOS reliability concerns. A later review notes that the phenomenon had been known since 1966, but became much more consequential as gate fields, operating temperatures, device structures, and gate-dielectric technology changed.[^nigam]

The reliability lesson is easy to miss because BTI can accumulate under sustained electrical bias even without the dramatic high-field transition associated with hot-carrier stress.

```text
biased transistor
+ temperature
+ time
-> threshold / drive drift
```

## Idle is not necessarily unstressed

Digital thinking often divides time into:

- useful switching;
- idle waiting.

BTI complicates that division.

A transistor held in a stressed bias state can accumulate degradation while the logic function appears to be doing nothing.

That makes workload history more subtle:

```text
switching activity
is one stress dimension

state residency
is another
```

A power-management state, always-on control path, SRAM cell, clock-gating structure, or long-lived logic condition can therefore have a reliability signature that is not captured by counting transitions alone.

## Recovery makes measurement difficult

BTI is also historically interesting because degradation can partially recover after stress is removed.

That means the measured result depends on **when** measurement occurs.

Later NBTI literature emphasized that delays between removing stress and measuring the device could materially change the apparent degradation.[^nigam]

So even the act of measurement became part of the reliability problem:

```text
stress
-> remove bias
-> recovery begins
-> measurement delay
-> reported degradation
```

Two laboratories can therefore disagree without either having simply “measured wrong” if their timing protocols differ.

## Reliability became a state-machine problem

At the product level, BTI encourages a different abstraction:

```text
device lifetime
= function(
    voltage,
    temperature,
    fraction of time in each state,
    recovery opportunity,
    process distribution
  )
```

This helps explain why reliability engineering increasingly interacts with:

- clock gating;
- power gating;
- duty-cycle balancing;
- standby states;
- voltage selection;
- thermal management;
- guard bands.

A transistor is not only a switch. It is a material system with memory of bias history.

## Engineering reconstruction

The experiment in [`../../experiments/bti-duty-cycle/`](../../experiments/bti-duty-cycle/) uses a synthetic stress/recovery accumulator.

It compares three toy workloads:

- nearly always stressed;
- alternating stress and recovery;
- mostly idle in an unstressed state.

No parameter is calibrated to a semiconductor technology. The purpose is only to show that identical elapsed time can produce different accumulated state depending on duty cycle and recovery.

## What became invisible

Modern users see a processor sleep state, voltage table, or reliability guard band.

Underneath that interface sit decades of work on:

```text
interface traps
oxide charge
bias stress
recovery
measurement timing
accelerated qualification
compact aging models
state residency
```

The remarkable thing is not that transistors age.

It is that industry learned enough about that aging to sell billions of systems whose expected lifetime can be designed rather than merely hoped for.

## Source caution

BTI mechanisms and models remain technology-dependent and historically contested in detail. This article preserves the engineering problem and measurement difficulty, not one universal microscopic explanation.

[^nigam]: T. Grasser and collaborators' broader literature is extensive; for a concise historical review see D. K. Schroder, “Negative bias temperature instability: What do we understand?”, *Microelectronics Reliability* 47 (2007), which notes that NBTI had been known since 1966 and discusses stress/recovery measurement issues, https://doi.org/10.1016/j.microrel.2006.10.006 .
