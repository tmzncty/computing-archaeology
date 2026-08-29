# Speed Infrastructure Field Set — Source Map

This field set traces how the pursuit of lower latency and higher throughput moved constraints outward from the transistor into pattern statistics, power, memory, packaging, optics, rack power, coolant, and network collectives.

Repository policy still applies: historical record, engineering reconstruction, and experiment must remain distinct.

## EUV stochastic / pellicle

- Imec, 2021, 0.33NA EUV single-exposure and stochastic electrical correlation: https://www.imec-int.com/en/press/imec-pushes-single-exposure-patterning-capability-033na-euvl-its-extreme-limits
- Imec, 2025, High-NA electrical yield / stochastic breaks and bridges: https://www.imec-int.com/en/press/imec-demonstrates-electrical-yield-20nm-pitch-metal-lines-obtained-high-na-euv-single
- ASML, 2022, EUV pellicle history: https://www.asml.com/news/stories/2022/the-euv-pellicle-indistinguishable-from-magic
- ASML, Q1 2021, 90% pellicle transmission as HVM productivity milestone: https://www.asml.com/en/news/press-releases/2021/q1-2021-financial-results

Caution: ASML material is corporate platform history. Imec's experimental work is stronger evidence for stochastic-yield mechanisms. No synthetic experiment parameters are scanner specifications.

## Backside power

- Imec, “How to power chips from the backside”: https://www.imec-int.com/en/articles/how-power-chips-backside
- Imec, 2021 backside-power building blocks: https://www.imec-int.com/en/articles/imec-demonstrates-critical-building-blocks-backside-power-delivery-network

Use: mechanism, process building blocks, and routing/IR-drop motivation. Do not treat one research vehicle as universal production implementation.

## Forksheet / CFET

- Imec, CFET roadmap: https://www.imec-int.com/en/articles/imec-puts-complementary-fet-cfet-logic-technology-roadmap
- Imec, outer-wall forksheet / 2025 roadmap: https://www.imec-int.com/en/articles/outer-wall-forksheet-bridge-nanosheet-and-cfet-device-architectures-logic-technology

Use: research-roadmap evidence. These are not claims that CFET is already ubiquitous production technology.

## HBM4

- Micron HBM4 current product page: https://www.micron.com/products/memory/hbm/hbm4
- SK hynix, 12 Sep 2025 HBM4 development / mass-production readiness: https://news.skhynix.com/en/sk-hynix-completes-worlds-first-hbm4-development-and-readies-mass-production/

Use: current vendor implementation evidence. Avoid turning vendor superlatives into neutral industry priority claims.

## Hybrid bonding / KGD

- TSMC SoIC: https://3dfabric.tsmc.com/chinese/dedicatedFoundry/technology/SoIC.htm
- Intel Foundry fact sheet: https://www.intel.com/content/www/us/en/foundry/library/fact-sheet.html
- Intel Foveros Direct 3D: https://www.intel.com/content/www/us/en/foundry/packaging.html

Use: vendor evidence for their own flows, fine pitch, and known-good-die/test emphasis.

## Co-packaged optics / external laser

- OIF 3.2T CPO IA, 2023: https://www.oiforum.com/oif-launches-the-industrys-first-co-packaging-standard-the-3-2t-co-packaged-module-implementation-agreement/
- OIF ELSFP IA, 2023: https://www.oiforum.com/oif-announces-external-laser-small-form-factor-pluggable-elsfp-implementation-agreement-paving-the-way-for-advancements-in-co-packaged-optics-applications/
- OIF implementation-agreement index: https://www.oiforum.com/technical-work/implementation-agreements-ias/

Use: standards-organization evidence for interoperability boundaries, not every proprietary CPO product.

## 224G / 448G electrical channels

- OIF CEI-224G and CEI-448G framework index: https://www.oiforum.com/documents/informative-documents/technical-white-papers-requirements-framework-errata/

Important: OIF explicitly labels framework documents as informative documents, not final Implementation Agreements.

## 800 VDC rack power

- Open Compute Project, 11 Aug 2026, Google/Microsoft/NVIDIA collaboration around 800 VDC: https://www.opencompute.org/index.php/blog/powering-the-next-era-of-ai-how-google-microsoft-and-nvidia-are-standardizing-and-accelerating-the-industry-transition-to-lvdc

Use: current open-infrastructure standardization direction. Do not project 800 VDC backward onto earlier AI racks.

## CDU / coolant chemistry

- OCP ACS Liquid Cooling Cold Plate Requirements: https://www.opencompute.org/documents/ocp-acs-liquid-cooling-cold-plate-requirements-pdf
- OCP Cold Plate workstream / coolant fluids: https://www.opencompute.org/wiki/Cooling_Environments/Cold_Plate

Use: mature open rack-cooling requirements and workstreams.

## In-network collective computation

- NVIDIA SHARP current introduction: https://networking-docs.nvidia.com/sharpum/3150/introduction
- NVIDIA NCCL NVLink SHARP control: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html

Use: vendor evidence for NVIDIA's own in-network and NVSwitch collective offload. The broader idea of in-network computing requires separate cross-vendor history before priority claims.

## Experiment boundary

All ten new experiments are synthetic teaching models. They demonstrate structural pressure only and must not be cited as scanner yield models, transistor-density forecasts, HBM4 electrical models, hybrid-bond yield forecasts, CPO link budgets, CEI compliance calculations, HVDC designs, coolant specifications, or collective-performance benchmarks.
