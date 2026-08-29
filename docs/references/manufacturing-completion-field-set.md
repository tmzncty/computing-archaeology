# Manufacturing Completion Field Set — Source Map

This source map covers the final first-pass manufacturing/reliability completion tranche.

It follows repository policy:

1. historical record;
2. engineering reconstruction;
3. experiment;

must remain distinct.

## 1. TDDB

### Sources

- A. Teramoto et al., “Time-dependent dielectric breakdown of SiO2 films in a wide electric field range,” *Microelectronics Reliability* 41, no. 1 (2001), 47–52. DOI: 10.1016/S0026-2714(00)00095-0.
- “Investigation of the intrinsic SiO2 area dependence using TDDB testing and model integration into the design process,” *Microelectronics Reliability* 38 (1998), 1121–1125. DOI: 10.1016/S0026-2714(98)00140-1.

### Use

These are reliability-literature anchors for stress-time, field/temperature acceleration and area dependence.

### Caution

Do not present one acceleration law as universal across oxide thicknesses, materials or device generations.

---

## 2. Hot-carrier degradation

### Sources

- K.-L. Chen et al., “Reliability Effects on MOS Transistors Due to Hot-Carrier Injection,” *IEEE Journal of Solid-State Circuits* 20, no. 1 (1985), 306–313. DOI: 10.1109/JSSC.1985.1052307.
- A. Acovic, G. La Rosa, Y.-C. Sun, “A review of hot-carrier degradation mechanisms in MOSFETs,” *Microelectronics Reliability* 36 (1996), 845–869. DOI: 10.1016/0026-2714(96)00022-4.

### Use

The 1985 paper anchors period engineering concern; the 1996 review is later synthesis.

### Caution

Do not collapse electron/hole injection, interface damage, oxide trapping and later device structures into one timeless mechanism.

---

## 3. Bias-temperature instability

### Source

- D. K. Schroder, “Negative bias temperature instability: What do we understand?”, *Microelectronics Reliability* 47 (2007). DOI: 10.1016/j.microrel.2006.10.006.

### Use

Later review used to establish that NBTI had been known since 1966 and to document stress/recovery measurement difficulty.

### Caution

This is retrospective synthesis, not a substitute for the original 1960s papers.

---

## 4. Alpha-particle soft errors

### Source

- T. C. May and M. H. Woods, “Alpha-particle-induced soft errors in dynamic memories,” *IEEE Transactions on Electron Devices* 26 (1979), 2–9. DOI: 10.1109/T-ED.1979.19370.

### Use

Near-primary period source connecting trace uranium/thorium in package material to alpha-induced charge deposition and DRAM/CCD soft errors.

### Caution

Do not treat package alpha emission as the only modern soft-error source; later cosmic-ray and neutron mechanisms are separate histories.

---

## 5. Moisture / popcorn cracking

### Source

- IPC/JEDEC J-STD-033C-1, *Handling, Packing, Shipping, and Use of Moisture/Reflow and/or Process Sensitive Components* (2014), public TOC/foreword copy: https://www.ipc.org/TOC/IPC-JEDEC-J-STD-033C-1.pdf .

### Use

Mature standardization evidence connecting SMD reflow, moisture diffusion, cracking/delamination, floor life and dry packing.

### Caution

Do not back-project current MSL terminology and current revision requirements onto early surface-mount factories.

---

## 6. Lead-free solder transition

### Sources

- C. A. Handwerker, D. Noctor, G. Whitten, “Reliability of Lead-Free Solders,” NIST (2001), https://www.nist.gov/publications/reliability-lead-free-solders .
- European Parliament and Council, Directive 2002/95/EC (RoHS), original/historical text through EUR-Lex: https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32002L0095 .

### Use

NIST anchors the early reliability uncertainty and context-dependent fatigue rankings; RoHS anchors regulatory pressure and exemptions.

### Caution

Do not reduce the global lead-free transition to RoHS alone or imply one universal replacement alloy.

---

## 7. Tin whiskers

### Sources

- NASA NEPP, “Basic Information Regarding Tin Whiskers,” https://nepp.nasa.gov/whisker/background/index.htm .
- NASA NEPP, “Tin Whisker Anecdote: 20 Years to Failure,” https://nepp.nasa.gov/WHISKER/anecdote/20year/index.html .
- NASA Parts Selection List, “Pure Tin Plating Prohibition,” https://nepp.nasa.gov/npsl/prohibited/tin_prohibition.htm .

### Use

Institutional reliability archive and documented failure evidence.

### Caution

NASA guidance reflects high-reliability/aerospace risk posture and should not be silently generalized into every consumer-electronics procurement policy.

---

## 8. Conductive anodic filamentation (CAF)

### Sources

- IPC-TM-650 Method 2.6.25B, *Conductive Anodic Filament (CAF) Resistance Test: X-Y Axis*, https://www.ipc.org/sites/default/files/test_methods_docs/2.6.25b.pdf .
- Laura J. Turbini, “Conductive Anodic Filament (CAF) Formation: An Historic Perspective,” IPC APEX EXPO 2005; IPC conference archive material: https://www.ipc.org/system/files/technical_resource/E17%26S02-3.pdf .

### Use

IPC test method establishes mature standardization; the historical paper preserves the late-1970s failure lineage.

### Caution

CAF is internal laminate filamentation and must not be conflated with surface ECM/dendrites.

---

## 9. Surface electrochemical migration / cleanliness

### Sources

- X. He, M. H. Azarian, M. G. Pecht, “Comparative Assessment of Electrochemical Migration on Printed Circuit Boards with Lead-Free and Tin-Lead Solders,” IPC technical paper, https://www.ipc.org/system/files/technical_resource/E8%26S14_02.pdf .
- X. He, M. H. Azarian, M. Kostinovsky, M. G. Pecht, “An Evaluation of the Insulation Resistance and Surface Contamination of Printed Circuit Board Assemblies,” IPC APEX EXPO 2012 summary, https://www.ipc.org/node?page=279 .

### Use

Documents metal dissolution/transport/deposition, dendrite formation, SIR, humidity/bias, flux residues and contamination measurement.

### Caution

Do not claim every visible residue is electrically harmful; chemistry, humidity, bias and geometry matter.

---

## 10. Connector fretting / contact metallurgy

### Sources

- M. Antler, “Fretting corrosion of gold-plated connector contacts,” *Wear* 74 (1981), 27–50. DOI: 10.1016/0043-1648(81)90192-7.
- M. Antler, “Electrical effects of fretting connector contact materials: A review,” *Wear* 106 (1985), 5–33. DOI: 10.1016/0043-1648(85)90101-2.
- NASA-STD-6016C, later aerospace workmanship guidance on gold/tin separable interfaces.

### Use

The Antler papers provide period/near-period contact-fretting engineering; NASA is later mature high-reliability practice.

### Caution

Vendor/contact systems differ. Gold is not a magic universal answer; plating stack, force, wipe, lubrication, substrate and environment all matter.

---

## 11. LGA sockets

### Sources

- Intel, *LGA775 Socket Mechanical Design Guide*, circa 2005, https://www.intel.com/Assets/PDF/designguide/302666.pdf .
- S. Yang, J. Wu, M. G. Pecht, “Reliability Assessment of Land Grid Array Sockets Subjected to Mixed Flowing Gas Environment,” *IEEE Transactions on Reliability* 58, no. 4 (2009), 634–640; CALCE abstract: https://calcetalk.umd.edu/articles/abstracts/2009/Reliability_Assess_LandGridArray_abstract.html .

### Use

Intel guide is primary corporate platform documentation for mechanical/socket constraints; CALCE paper covers later accelerated corrosion/contact-resistance behavior.

### Caution

LGA775 dimensions must not be generalized to all LGA sockets.

---

## 12. TIM aging

### Source

- “Reliability of thermal interface materials: A review,” *Applied Thermal Engineering* (2012), https://www.sciencedirect.com/science/article/pii/S1359431112004346 .

### Use

Later synthesis for pump-out, dry-out, temperature, mechanical loading and TIM reliability mechanisms.

### Caution

TIM families differ greatly; a grease mechanism is not automatically a pad, phase-change material or solder-TIM mechanism.

---

## 13. Heat pipes / vapor chambers

### Sources

- G. M. Grover, U.S. Patent 3,229,759, “Evaporation-condensation heat transfer device,” filed December 2, 1963, https://patents.google.com/patent/US3229759A/en .
- Later historical review of heat-pipe development: https://www.sciencedirect.com/science/article/pii/S0306454921002693 .

### Use

Grover patent is primary period evidence; later review supplies historical context and subsequent application spread.

### Caution

Do not call every thermosyphon or pre-1963 evaporation-condensation device a Grover heat pipe, and do not erase Gaugler/earlier thermosyphon ancestry.

---

## 14. Copper roughness / glass weave

### Sources

- Intel/Altera, *High-Speed Board Design Advisor: High-Speed Channel Design and Layout*, https://cdrdv2-public.intel.com/652630/tb-095.pdf .
- Intel, “Fiberglass Weave Composition,” https://www.intel.com/content/www/us/en/docs/programmable/683883/current/fiberglass-weave-composition.html .
- IPC conference material, “The Effect of Radiation Losses on High Frequency PCB Performance,” https://www.ipc.org/system/files/technical_resource/E15%26S30_01.pdf .

### Use

Modern engineering guidance documenting the transition from idealized board traces to frequency-dependent material/channel behavior.

### Caution

These are mature high-speed design sources, not evidence that early digital boards were designed using modern multi-gigabit terminology.

---

## 15. Via stubs / backdrilling

### Source

- IPC / ECWC conference paper on backdrilling and unused plated-through-hole length, https://www.ipc.org/system/files/technical_resource/E17%26S25-3.pdf .

### Use

Documents via-stub influence on high-frequency impedance, insertion loss and crosstalk and the manufacturing use of controlled-depth drilling.

### Caution

The teaching experiment uses only a quarter-wave proxy. Real via behavior requires full geometry, reference planes, pads, anti-pads, return paths, material loss and mode conversion.

---

# Cross-field cautions

## Later standards are not early history

J-STD, IPC-TM-650, Intel platform guides and NASA standards often represent mature institutional practice. They are invaluable for understanding what eventually became standardized, but they must not be presented as if the same terminology and limits existed at the phenomenon's first discovery.

## Corporate sources are interested sources

Intel platform guides are primary evidence for Intel platform requirements, not neutral evidence of industry priority. NASA is authoritative for its own reliability posture, not universal consumer practice.

## Experiments expose topology, not truth tables for industry

Every new experiment in this tranche uses synthetic parameters. They exist to expose constraint structure:

```text
stress -> lifetime
state residency -> aging
particle charge -> upset
moisture -> reflow stress
context -> solder ranking
long-tail growth -> bridge
humidity+bias -> migration
force+wear -> contact resistance
population spread -> socket yield
cycling -> TIM degradation
capillary return -> heat transport
material microstructure -> high-speed loss/skew
stub length -> resonance
```

They are not qualification, safety, lifetime, process or product design tools.
