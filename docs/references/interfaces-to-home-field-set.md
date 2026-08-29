# Interfaces to Home — Field-Set Source Map

This source map supports the excavation round that connects atom-scale contact/interconnect fabrication to package, PCB, and consumer thermal interfaces.

It is a research map, not a substitute for article-level footnotes.

## Source discipline

This field set deliberately mixes several evidence types because no single archive covers the whole chain.

1. **Patents / near-period technical disclosures** are used for process structure and historical engineering constraints.
2. **Research publications** are used for materials-integration problems and production-adjacent development.
3. **Industry standards / institutional history** are used for mature PCB and assembly practice.
4. **Modern vendor engineering material** is used only to document later stable practice, equipment families, and terminology.
5. **Corporate histories / product announcements** are treated as evidence of what the company reported implementing, not as neutral priority histories.

Synthetic experiments in this field set do not reproduce historical process dimensions or commercial recipes.

---

## Tungsten contacts and WF6

### US9978605B2 — tungsten fill background

https://patents.google.com/patent/US9978605B2/en

Use for:

- tungsten fill in contacts / recessed features;
- nucleation-layer concept;
- later process description showing continuity between contact geometry and deposition strategy.

Source type: later patent background. Useful for stable process structure, **not** for dating the first tungsten contact.

### US6464778B2 — WF6 tungsten deposition

https://patents.google.com/patent/US6464778B2/en

Use for:

- WF6-based tungsten growth;
- silane / hydrogen reduction context;
- staged tungsten nucleation / growth reasoning.

Source type: patent disclosure.

### US6429126B1 — fluorine contamination

https://patents.google.com/patent/US6429126B1/en

Use for:

- fluorine contamination concern at tungsten / TiN / Ti integration interfaces;
- evidence that precursor chemistry can damage neighboring layers.

Source type: patent disclosure.

---

## Hidden barrier / liner metals

### US5240880A — Ti/TiN contact metallization

https://patents.google.com/patent/US5240880A/en

Use for:

- titanium / titanium nitride contact stacks;
- explicit deposition into contact openings;
- historical evidence that the electrical contact was already a multi-material interface.

Source type: near-period patent disclosure.

### IBM low-k / copper integration review

https://research.ibm.com/publications/progress-in-the-development-and-understanding-of-advanced-low-k-and-ultralow-k-dielectrics-for-very-large-scale-integrated-interconnects-state-of-the-art

Use for:

- copper replacing aluminum in late-1990s interconnect technology;
- later low-k introduction;
- integration tradeoffs among copper, dielectric, mechanical strength, and process compatibility.

Source type: later IBM research review by participants / institutional researchers. Valuable retrospective, not a sole-source priority authority.

---

## Low-k and high-k dielectric divergence

### Intel 45 nm high-k / metal-gate announcement, 2007

https://www.intel.com/pressroom/archive/releases/2007/20070128comp.htm

Use for:

- Intel's stated transition from ultrathin SiO2 to hafnium-based high-k gate dielectric;
- approximately 1.2 nm prior SiO2 gate dielectric context;
- metal-gate co-introduction;
- gate leakage as a scaling constraint.

Source type: corporate product / technology announcement. Strong evidence for Intel's implementation and self-described rationale; not neutral industry-wide invention history.

### IBM low-k review

Same IBM URL above.

Use for:

- RC interconnect bottleneck;
- SiCOH / porous low-k lineage;
- reduced mechanical / chemical robustness of ultralow-k materials.

### US4872947A — TEOS oxide CVD

https://patents.google.com/patent/US4872947A/en

Use for:

- late-1980s TEOS-based deposited silicon oxide process context;
- evidence that “SiO2” can refer to very different production routes and roles.

Source type: patent disclosure.

---

## Backside helium and wafer thermal interface

### US5856906A — backside gas cooling

https://patents.google.com/patent/US5856906A/en

Use for:

- inert backside gas, especially helium;
- electrostatic chuck plus backside gas interaction;
- water-cooled support / pedestal context;
- local leakage as a cause of thermal non-uniformity;
- gas release / dump as part of wafer-handling sequence.

Source type: near-period equipment patent. It documents mature technique and constraints, not a universal invention date.

---

## Vacuum pump evolution

### Leybold — diffusion versus turbomolecular history

https://www.leybold.com/en-us/knowledge/blog/when-is-a-diffusion-pump-the-right-choice

Use for:

- vendor institutional account that turbomolecular pumps became commercially viable in the 1970s and displaced diffusion pumps in some cleaner high-vacuum roles.

Source type: modern vendor technical history. Use cautiously for chronology; corroborate priority claims elsewhere before strengthening them.

### Leybold — turbomolecular pump engineering

https://www.leybold.com/en-us/knowledge/blog/turbomolecular-pumps-what-you-need-to-know

Use for:

- modern turbo-pump compression / backing-pump system structure;
- oil-free high-vacuum mechanism context.

Source type: modern vendor engineering.

### Edwards — semiconductor vacuum product families

https://www.edwardsvacuum.com/en-us/semiconductor

Use for:

- mature semiconductor use of dry pumps, turbo pumps, cryopumps, abatement, and subfab support.

### Edwards — pump maintenance / harsh process evidence

https://www.edwardsvacuum.com/en-ca/semiconductor/knowledge/innovation-hub/predictive-maintenance-reduced-costs-casestory

https://www.edwardsvacuum.com/en-ca/news-and-events/semicon-china-pressrelease

Use for:

- modern evidence that pump state affects tool uptime / wafer loss;
- harsh / condensable process loads as a pump-design concern.

Source type: current vendor material; **do not project product-specific claims backward into early semiconductor fabs**.

---

## Laser microvias, desmear, and electroless copper

### IPC/JPCA-4104 revision record

https://www.ipc.org/ipc-document-revision-table

Use for:

- institutional evidence that HDI / microvia materials had become a distinct standardization problem by the late 1990s.

### IPC-9121A troubleshooting table of contents

https://www.ipc.org/TOC/IPC-9121A_TOC.pdf

Use for:

- laser-drill microvia defects;
- target-pad damage;
- microvia plating separation;
- electroless-copper process problem categories.

Source type: modern troubleshooting standard / handbook.

### IPC APEX 2009 — electroless copper sequence

https://www.ipc.org/node?page=316

Use for:

- desmear;
- cleaning / conditioning;
- activation;
- electroless copper;
- the bootstrapping role of conductive seed on nonconductive via walls.

Source type: mature industry technical paper.

---

## Solder paste and flux

### IPC history

https://www.ipc.org/ipc-history

Use for:

- institutional history of surface-mount manufacturing and adoption of joint industry solder / flux / paste standards.

### IPC current standards listing

https://www.ipc.org/recently-released-ipc-standards-and-documents

Use for:

- continuing separation of soldering-flux and solder-paste specifications (J-STD-004 / J-STD-005).

Source type: current standards infrastructure, not historical composition data.

### Rick Lathrop — “The Digital Solder Paste”

https://www.ipc.org/system/files/technical_resource/E8%26S19_01.pdf

Use for:

- retrospective industry statement that solder paste has been integral to SMT for decades;
- formulation / mixture / rheology complexity.

Source type: later industry technical paper.

---

## Underfill and package mechanics

### IBM ECTC 2011 wafer-level underfill

https://research.ibm.com/publications/development-of-wafer-level-underfill-materials-and-assembly-processes-for-fine-pitch-pb-free-solder-flip-chip-packaging

Use for:

- filler loading;
- void control;
- flip-chip joining sequence;
- thermal-cycle / humidity / storage reliability evaluation;
- evidence that underfill is both a material and a process window.

### IBM ECTC 2012 ultra-low-k / Cu-pillar underfill

https://research.ibm.com/publications/wafer-level-underfill-for-area-array-cu-pillar-flip-chip-packaging-of-ultra-low-k-chips-on-organic-substrates

Use for:

- protecting interconnect and BEOL structures;
- coupling package mechanics to fragile ultra-low-k die structures;
- void-free packaging challenge.

Source type: production-adjacent research paper.

Do not project 2010s wafer-level-underfill formulations backward onto early C4 history.

---

## TIM, lid attach, and consumer thermal interface

### Intel — package manufacturing overview

https://newsroom.intel.com/tech101/how-silicon-die-become-chip-packages

Use for:

- modern lid attach sequence;
- TIM between die and heat spreader;
- burn-in / final test context.

Source type: corporate educational material describing modern Intel package practice.

### Intel — TIM support guidance

https://www.intel.com/content/www/us/en/support/articles/000005576/processors.html

Use for:

- TIM as thermal exchange interface between integrated heat spreader and fan-heatsink;
- sensitivity to contamination / installation.

Source type: modern product-support guidance. Not a historical TIM formulation source.

---

## Cross-source cautions

### 1. A later process description is not an invention date

Tungsten, barrier, vacuum, underfill, and PCB sources frequently document a mature process decades after its earliest development.

Use them to establish **mechanism and mature industrial structure**, not unsupported “first” claims.

### 2. Company implementation is not universal industry chronology

Intel high-k and IBM underfill / low-k sources document specific corporate programs and technical lineages.

They should not be rewritten as if every manufacturer changed materials simultaneously.

### 3. Modern standards are not early-factory specifications

IPC standards and troubleshooting material help show which variables became formalized.

They do not prove those exact limits existed in early SMT or early HDI production.

### 4. The experiments are explanatory, not calibration

Every experiment in this round uses synthetic normalized values.

None is suitable for:

- wafer-process design;
- vacuum sizing;
- solder-paste selection;
- PCB desmear / plating recipes;
- underfill selection;
- processor thermal design;
- reliability qualification.

## Preservation lesson

This field set crosses an unusually wide industrial span:

```text
WF6 cylinder
→ tungsten contact
→ barrier metal
→ dielectric stack
→ backside helium
→ vacuum pump
→ laser microvia
→ solder paste
→ underfill
→ TIM / lid
→ consumer heatsink
```

The historical danger is that each specialist literature preserves only its own segment.

The repository's job is to preserve the **dependency chain** without pretending the chain was designed by one organization or invented in one moment.
