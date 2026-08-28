# Manufacturing Substrate Field Set 5 — Purity, Facilities, and the Artificial Environment

This source map supports the fifth manufacturing excavation set:

- ultrapure water;
- continuous clean-air control;
- high-purity specialty-gas distribution;
- vacuum cleanliness;
- temperature / cooling / vibration stability;
- electrostatic / electromagnetic control;
- exhaust and abatement;
- the fab facility layer as a synthesis.

The central research question is:

> **What infrastructure had to become controlled, measurable, and repeatable before the semiconductor process could treat the surrounding factory as a stable environment rather than an uncontrolled source of contamination and drift?**

## Source-handling rule for this field set

Facilities history is unusually easy to distort because many useful public sources are later standards, safety guidance, supplier literature, or institutional retrospectives.

Use them for the right purpose:

```text
period government / technical report
    -> what the industry was actually doing or regulating at that time

period journal / engineering paper
    -> contemporary mechanism / engineering problem

later institutional retrospective
    -> chronology and preservation context, with caveat

SEMI / ASHRAE standard or guide
    -> mature industry interface / control practice, not proof of early practice

OSHA guidance / accident record
    -> operational hazards and real maintenance consequences

supplier / application note
    -> modern implementation examples only; never historical authority
```

## 1. Ultrapure water

### U.S. EPA, 1983 semiconductor subcategory

- *Development Document for Effluent Limitations Guidelines and Standards for the Electrical and Electronic Components Point Source Category, Phase I* (1983):
  https://www.epa.gov/sites/default/files/2016-05/documents/eec_phase_1_dd_apr_1983.pdf
- Text mirror:
  https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=000014ER.TXT

Useful for period evidence that plant incoming water was deionized for semiconductor processing and used for:

- acid formulation;
- wafer rinsing;
- cleaning equipment/materials;
- exhaust collection;
- slicing/lapping/dicing support.

Source type: U.S. government period industrial/environmental document.

Caveat: written for effluent-regulation development, not as a UPW engineering manual.

### U.S. EPA industrial-process profile

- *Industrial Process Profiles for Environmental Use: Chapter 30, The Electronic Component Manufacturing Industry*:
  https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=9101NTZM.TXT

Useful period description of semiconductor UPW resistivity control and rinsing practice.

Source type: period government industrial profile.

### SEMI UPW guides

- SEMI F61 — design/operation of semiconductor UPW systems:
  https://store-us.semi.org/products/f06100-semi-f61-guide-to-design-and-operation-of-a-semiconductor-ultrapure-water-system
- SEMI F63 — UPW quality:
  https://store-us.semi.org/products/f06300-semi-f63-guide-for-ultrapure-water-used-in-semiconductor-processing
- SEMI F75 — UPW monitoring:
  https://store-us.semi.org/products/f07500-semi-f75-guide-for-quality-monitoring-of-ultrapure-water-used-in-semiconductor-manufacturing
- SEMI F98 — reuse-water treatment:
  https://store-us.semi.org/products/f09800-semi-f98-guide-for-treatment-of-reuse-water-in-semiconductor-processing

Source type: mature industry standards/guides.

Use for:

- treatment/distribution/point-of-use becoming one controlled system;
- contaminant monitoring beyond resistivity;
- formalization of water reuse.

Do not project modern quality numbers backward into 1970s/1980s fabs.

### Later process-integration caution

- T. Hattori, “Ultrapure Water-Related Problems and Waterless Cleaning Challenges,” *ECS Transactions* 34(1), 2011; EPA HERO record:
  https://hero.epa.gov/reference/2643109/

Use to show that UPW itself can become an integration constraint at advanced geometry (flow electrification, watermarking, corrosion, pattern collapse, material interactions).

Source type: later technical paper.

## 2. Clean air and laminar / unidirectional flow

### Sandia / Willis Whitfield history

- Sandia Lab News, “Willis Whitfield, inventor of modern-day laminar-flow clean room, passes away,” 2012:
  https://www.sandia.gov/labnews/2012/11/16/12-16-11-2/
- Sandia 75 Ways historical page:
  https://www.sandia.gov/75-ways/sandia-making-history/
- 2024 Sandia historical feature:
  https://www.sandia.gov/labnews/2024/04/04/willis-whitfield-a-simple-man-with-a-simple-solution-that-changed-the-world/

Useful for:

- 1959–1961 contamination problem and prototype chronology;
- the conceptual move from sealed/turbulent rooms to continuously swept highly filtered airflow;
- period-derived filter/particle-count details;
- institutional technology-transfer history.

Source type: later institutional retrospective based on Sandia archives/interviews.

Caveat: Sandia is documenting its own institution and inventor; do not treat promotional language as neutral historiography.

### ASHRAE clean-space guidance

- ASHRAE Handbook, “Clean Spaces”:
  https://handbook.ashrae.org/Handbooks/A23/SI/a23_ch19/a23_ch19_si.aspx

Useful for mature facility concepts:

- semiconductor fab temperature/humidity stability;
- environmental control as dimensional/process control;
- modern clean-space design vocabulary.

Source type: later engineering handbook.

## 3. High-purity and specialty gases

### OSHA semiconductor process guidance

- Silicon device fabrication:
  https://www.osha.gov/semiconductors/silicon/device-fabrication
- CVD gas table:
  https://www.osha.gov/semiconductors/tables/table6

Useful for identifying common process/source/dopant gases and operational hazards:

- silane;
- ammonia;
- nitrogen / hydrogen carrier gas;
- arsine;
- phosphine;
- diborane;
- corrosive / toxic reaction products.

Source type: later U.S. operational safety guidance.

### SEMI gas-distribution standards

- SEMI F22 — bulk/specialty gas distribution (originally 1997):
  https://store-us.semi.org/products/f02200-semi-f22-guide-for-bulk-and-specialty-gas-distribution-systems
- SEMI F13 — gas source control equipment (originally 1993):
  https://store-us.semi.org/products/f01300-semi-f13-guide-for-gas-source-control-equipment
- SEMI F14 — gas source equipment enclosures (originally 1993):
  https://store-us.semi.org/products/f01400-semi-f14-guide-for-the-design-of-gas-source-equipment-enclosures

Useful for showing mature standardization of:

- source-to-tool distribution;
- hazardous gas controls;
- cabinets/enclosures;
- valves / containment / leak-integrity concepts.

Source type: industry standards.

### Maintenance accident evidence

- OSHA semiconductor epitaxial-reactor exhaust incident:
  https://www.osha.gov/ords/imis/accidentsearch.accident_detail?id=202315461

Useful for showing that exhaust/pump residues can differ materially from source gas and become unstable during maintenance.

Source type: accident investigation record.

## 4. Vacuum cleanliness

### Diffusion-pump contamination

- “Diffusion pump back-streaming,” *Vacuum* 27(9), 1977, pp. 519–530:
  https://www.sciencedirect.com/science/article/pii/S0042207X77804193

Useful for direct period evidence that pump working fluid could itself contaminate a high-vacuum system and that preventing backstreaming was a serious vacuum-engineering concern.

Source type: period technical review.

### Vacuum pump family overview

- ScienceDirect Topics, “Industrial Hygiene,” vacuum-pump section:
  https://www.sciencedirect.com/topics/engineering/industrial-hygiene

Useful only for broad orientation to mechanical, diffusion, getter/ion, turbo, and cryogenic pump families and a summarized industry progression.

Source type: tertiary technical synthesis.

Do not use for priority claims or exact historical adoption dates without primary corroboration.

## 5. Thermal, cooling, floor, and vibration stability

### ASHRAE semiconductor fab environment

- ASHRAE Handbook, “Clean Spaces”:
  https://handbook.ashrae.org/Handbooks/A23/SI/a23_ch19/a23_ch19_si.aspx

Use for mature temperature/humidity stability logic and environmental-condition examples.

### Semiconductor facilities energy/system inventory

- S.-C. Hu et al., “Power consumption benchmark for a semiconductor cleanroom facility system,” *Energy and Buildings* 40(9), 2008:
  https://www.sciencedirect.com/science/article/pii/S0378778808000662

Useful because the abstract explicitly treats the fab facility as a collection of:

- chilled water;
- air recirculation;
- make-up air;
- exhaust;
- compressed air;
- PCW;
- nitrogen;
- vacuum;
- UPW.

Source type: later field-measurement research.

### Fab structural vibration

- “Vibration analysis of waffle floors,” *Computers & Structures*:
  https://www.sciencedirect.com/science/article/pii/S0045794902003486

Useful for:

- vibration sources in fabs;
- photolithography-machine inertial forces;
- scanner-to-scanner vibration concerns;
- floor dynamic stiffness / damping / impedance as equipment-support requirements.

Source type: later structural-engineering research.

### Facility interface standardization

- SEMI E51 — typical facility services and termination matrix (first published 1995):
  https://store-us.semi.org/products/e05100-semi-e51-guide-for-typical-facilities-services-and-termination-matrix

Useful for showing the facilities/tool boundary becoming a formal equipment-procurement interface.

## 6. Static, ESD, ESA, and EMI

### SEMI E78

- SEMI E78 — ESD / electrostatic attraction for equipment (first published 1998):
  https://store-us.semi.org/products/e07800-semi-e78-guide-to-assess-and-control-electrostatic-discharge-esd-and-electrostatic-attraction-esa-for-equipment

Useful for mature industry recognition that static charge can cause:

- product/reticle ESD damage;
- equipment malfunction;
- particle attraction;
- cost-of-ownership effects.

### SEMI E129

- Facility-wide electrostatic-charge control:
  https://store-us.semi.org/products/e12900-semi-e129-guide-to-assess-and-control-electrostatic-charge-in-a-semiconductor-manufacturing-facility

Useful for facility materials, personnel, carriers, packaging, and equipment becoming part of one electrostatic-compatibility system.

### SEMI E33 / E176

- Equipment EMC, first published 1994:
  https://store-us.semi.org/products/e03300-semi-e33-guide-for-semiconductor-manufacturing-equipment-electromagnetic-compatibility-emc
- Broader fab EMI guidance:
  https://store-us.semi.org/products/e17600-semi-e176-guide-to-assess-and-minimize-electromagnetic-interference-emi-in-a-semiconductor-manufacturing-environment

Use as mature standards evidence for electrical environment becoming a manufacturing reliability/metrology issue.

### SEMI E163

- Extremely electrostatic-sensitive reticle/item handling:
  https://store-us.semi.org/products/e16300-semi-e163-guide-for-the-handling-of-reticles-and-other-extremely-electrostatic-sensitive-ees-items-within-specially-designated-areas

Useful for connecting lithography assets to electrostatic control.

## 7. Exhaust, ventilation, and abatement

### SEMI S6

- Exhaust ventilation of semiconductor manufacturing equipment, originally published 1993:
  https://store-us.semi.org/products/s00600-semi-s6-environmental-health-and-safety-guideline-for-exhaust-ventilation-of-semiconductor-manufacturing-equipment

Useful for the tool-to-facility exhaust interface and mature performance-based ventilation criteria.

### SEMI F5

- *Guide for Gaseous Effluent Handling*:
  https://store-us.semi.org/products/f00500-semi-f5-guide-for-gaseous-effluent-handling

Useful for:

- exhaust-stream separation;
- point-of-use vs end-of-pipe abatement;
- gaseous/particulate contaminant treatment;
- recovery / usage reduction.

Source type: industry guide.

### OSHA process hazard guidance

- https://www.osha.gov/semiconductors/silicon/device-fabrication

Useful for real process exhaust categories and maintenance-residue hazards.

### EPA water/exhaust coupling

The 1983 EPA semiconductor document is especially useful for one easy-to-miss connection: DI/UPW used as a medium for collecting exhaust gases from furnaces, solvents, and acid baths.

This demonstrates that fab “air,” “water,” and “waste” systems are coupled process infrastructures.

## 8. Facility-layer synthesis

- [`../facilities/why-the-fab-became-a-utility-machine.md`](../facilities/why-the-fab-became-a-utility-machine.md)

This article intentionally synthesizes rather than introduces a new priority claim.

Its evidence should be traced back to the topic-specific sources above.

## Experiments in this field set

- [`../../experiments/upw-contamination-budget/`](../../experiments/upw-contamination-budget/)
- [`../../experiments/airflow-removal/`](../../experiments/airflow-removal/)
- [`../../experiments/gas-delivery-purity/`](../../experiments/gas-delivery-purity/)
- [`../../experiments/vacuum-gas-load/`](../../experiments/vacuum-gas-load/)
- [`../../experiments/facility-stability-budget/`](../../experiments/facility-stability-budget/)
- [`../../experiments/static-particle-attraction/`](../../experiments/static-particle-attraction/)
- [`../../experiments/abatement-capacity/`](../../experiments/abatement-capacity/)

All experiment numbers are synthetic unless a README explicitly says otherwise.

None of these scripts is a design/qualification tool for a fab facility.

## Labor and preservation targets

Future source collection should actively recover the people behind “utilities normal”:

- UPW plant operators and water chemists;
- high-purity piping installers/welders;
- filter and resin technicians;
- cleanroom HVAC technicians;
- contamination-control engineers;
- specialty-gas technicians;
- gas-cabinet / detector technicians;
- orbital/GTA welders;
- vacuum technicians;
- pump rebuild/service workers;
- leak-check technicians;
- chiller and PCW operators;
- vibration/metrology engineers;
- ESD coordinators;
- ionizer / grounding technicians;
- exhaust-balancing technicians;
- scrubber/abatement operators;
- wastewater operators;
- subfab maintenance crews;
- facilities controls/BMS engineers;
- safety/interlock technicians.

The success state of these jobs is usually invisible: nothing contaminates the wafer, nothing drifts, nothing leaks, nothing overheats, and nothing catches fire.

That invisibility is exactly why the work needs explicit historical preservation.