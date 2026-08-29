# Why PAM4 Made Error Correction Part of the Link

For decades, faster serial links often meant making two-level signaling switch faster. PCIe 6.0 took a different step: four voltage levels, two bits per symbol, and an explicit acceptance that the raw channel would be harder to read reliably.

## Historical record

PCI-SIG states that PCIe 6.0 uses 64 GT/s PAM4 signaling, lightweight forward error correction (FEC), CRC, and FLIT-based encoding. PCI-SIG also explains that PAM4's expected raw BER is higher than earlier NRZ generations, motivating FEC/CRC and replay mechanisms.[^pcie][^fec]

## Engineering reconstruction

NRZ has two levels:

```text
0 ----
1 ----
```

PAM4 has four:

```text
00 ----
01 ----
10 ----
11 ----
```

Two bits per symbol increase data rate without doubling symbol frequency. But voltage spacing between adjacent levels shrinks, so noise/jitter consumes a larger fraction of each eye.

The architecture responds by moving reliability into coding and protocol:

```text
PAM4 physical channel
 -> FEC
 -> CRC
 -> replay when required
 -> FLIT framing
```

A 'wire' has become a layered error-management system.

## Experiment

[`experiments/pam4-margin/pam4_margin.py`](../../experiments/pam4-margin/pam4_margin.py) compares synthetic NRZ and PAM4 level spacing under equal full-scale voltage and adds a simplified FEC recovery proxy.

## Source caution

The experiment is not a PCIe BER/FEC implementation. Exact coding, latency, and compliance requirements belong to the specification.

[^pcie]: PCI-SIG, “PCI Express 6.0 Specification,” https://pcisig.com/pci-express-6.0-specification
[^fec]: PCI-SIG FAQ, “What is Forward Error Correction (FEC)...,” https://pcisig.com/what-forward-error-correction-fec-and-how-it-utilized-pcie-60-specification
