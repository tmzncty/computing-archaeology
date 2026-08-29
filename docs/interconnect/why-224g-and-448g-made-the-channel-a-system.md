# Why 224G and 448G Made the Channel a System

At extreme lane rates, the signal path cannot be treated as a cable plus two endpoints.

## Historical record

OIF published its CEI-224G framework in 2022 and a CEI-448G framework in November 2025. OIF explicitly classifies these framework documents as precursors/requirements work rather than final Implementation Agreements.[^oif]

## Engineering reconstruction

Faster signaling increases pressure from:

- insertion loss;
- return loss;
- crosstalk;
- package loss;
- connector discontinuities;
- jitter;
- equalization complexity;
- power per bit;
- test-instrument bandwidth.

The link therefore becomes a co-designed path:

```text
SerDes -> package -> PCB -> connector/cable -> PCB -> package -> SerDes
         equalization / coding / FEC / training / telemetry
```

## Speed connection

A nominal lane rate is not useful throughput if error correction, retransmission, or equalizer power becomes overwhelming. Channel speed therefore becomes a system budget.

## Experiment

`experiments/cei-rate-budget/cei_rate_budget.py` applies synthetic loss and equalization penalties as lane rate rises from 112 to 224 to 448 arbitrary units.

[^oif]: OIF, “Informative Documents,” https://www.oiforum.com/documents/informative-documents/technical-white-papers-requirements-framework-errata/
