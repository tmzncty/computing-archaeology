# Post-Scaling Field Set — Source Map

This source map covers the first-pass **post-planar-scaling → advanced package → rack infrastructure** extension.

Repository policy remains:

1. historical record;
2. engineering reconstruction;
3. experiment;

must be kept distinct.

## FinFET

- UC Berkeley contemporary 1999 institutional release: https://newsarchive.berkeley.edu/news/media/releases/99legacy/11-22-1999b.html
- Chenming Hu bibliography for the IEDM 1999 FinFET paper: https://www.chu.berkeley.edu/publication/

Use for prototype chronology and gate-control motivation. Do not treat the prototype as identical to later production nodes.

## GAA nanosheet

- IBM Research, Loubet et al., VLSI Technology 2017: https://research.ibm.com/publications/stacked-nanosheet-gate-all-around-transistor-to-enable-scaling-beyond-finfet

Use as near-primary research evidence for stacked horizontal nanosheets as a FinFET successor candidate.

## EUV / High-NA

- ASML EUV systems: https://www.asml.com/en/en/products/euv-lithography-systems
- ASML company history: https://www.asml.com/en/company/about-asml/history
- ASML lenses/mirrors explainer: https://www.asml.com/en/en/technology/lithography-principles/lenses-and-mirrors

Corporate technical history: strong for ASML product chronology and architecture; not neutral priority history.

## HBM / TSV

- SK hynix HBM development history: https://news.skhynix.com/en/the-story-of-sk-hynixs-hbm-development/
- AMD Radeon Fury/HBM product announcement, 2015: https://ir.amd.com/news-events/press-releases/detail/619/amd-ushers-in-a-new-era-of-pc-gaming-with-radeontm-r9-and-r7-300-series-graphics-line-up-including-worlds-first-graphics-family-with-revolutionary-hbm-technology

Corporate sources; priority wording must be treated as company claims. Use for product timing, TSV/HBM architecture, and market motivation.

## Silicon interposer / CoWoS

- TSMC CoWoS platform and chronology: https://3dfabric.tsmc.com/english/dedicatedFoundry/technology/cowos.htm

Use for TSMC platform history; not a universal interposer history.

## Hybrid bonding / SoIC / Foveros Direct

- TSMC SoIC: https://www.tsmc.com/english/dedicatedFoundry/technology/SoIC_inDepth
- Intel process/packaging announcement: https://www.intc.com/news-events/press-releases/detail/1486/intel-accelerates-process-and-packaging-innovations

Use as vendor implementation evidence. Keep platform names distinct from the generic process family.

## UCIe

- UCIe Consortium specifications: https://www.uciexpress.org/specifications

Normative/intended interface evidence for die-to-die standardization.

## PCIe 6 PAM4 / FEC / FLIT

- PCI-SIG PCIe 6.0 overview: https://pcisig.com/pci-express-6.0-specification
- PCI-SIG FEC FAQ: https://pcisig.com/what-forward-error-correction-fec-and-how-it-utilized-pcie-60-specification

Standards-organization material; use for signaling/protocol features, not vendor product claims.

## Retimers

- Astera Labs FAQ: https://www.asteralabs.com/resources/faqs/

Vendor engineering evidence for mature retimer budgeting and clock/data regeneration. PCI-SIG remains normative for PCIe behavior.

## Rack power

- NVIDIA H100 specs: https://www.nvidia.com/en-us/data-center/h100/
- OCP ORv3 rack example: https://www.opencompute.org/ai-marketplace/products/440/rittal-open-rack-v3-orv3
- OCP MGX rack specification: https://www.opencompute.org/documents/mgx-accelerated-computing-rack-and-trays-specification-1-1-pdf-1

Use to show the scale of contemporary module/rack power and the emergence of 48 V busbar systems.

## Cold plates / QDs

- OCP Cold Plate project: https://www.opencompute.org/wiki/Cooling_Environments/Cold_Plate
- OCP liquid-cooled ORv3 server example: https://www.opencompute.org/products/723/pegatron-ms303-2a1g-2ou-2-node-orv3-ai-gpu-server

Use for open infrastructure requirements and product examples, not as proof that all datacenters use the same loop.

## Cross-field caution

This field set is deliberately recent compared with the repository's early-computing material. Dates and platform generations matter. Avoid narrating still-evolving vendor roadmaps as settled historical inevitabilities.
