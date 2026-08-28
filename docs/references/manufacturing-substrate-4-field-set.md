# Manufacturing Substrate — Field Set 4 Source Map

This source map supports the fourth manufacturing excavation round:

- statistical process control / parametric feedback / yield learning;
- wafer probe and burn-in;
- electromigration;
- solder fatigue and package delamination;
- AOI / ICT / X-ray inspection;
- 300 mm FOUP / SECS-GEM / GEM300 / MES / traceability;
- GDSII / tape-out / mask-data preparation;
- advanced packaging and multi-die integration.

It records **source type and caveat**, not just URLs.

## 1. Process control, metrology, and yield learning

### NASA/JPL ASIC reliability guidance

- https://parts.jpl.nasa.gov/asic/Sect.4.3.html

Use for:

- statistical-control concepts in high-reliability semiconductor qualification;
- technology characterization vehicles/test structures;
- infant mortality and wear-out framing;
- burn-in discussion.

Source type: government engineering guidance for high-reliability/aerospace use.

Caveat: not a representative manual for all commercial fabs.

### NIST, semiconductor manufacturing systems

- https://www.nist.gov/publications/innovations-advanced-processes-and-systems-semiconductor-manufacturing

Use for modern framing of:

- in-line metrology;
- process control;
- manufacturing data analytics;
- advanced packaging and factory operation.

Source type: modern scholarly/institutional synthesis.

Caveat: useful for continuity and terminology, not direct evidence of 1960s–1980s fab practice.

### SEMI smart-manufacturing / FDC material

- https://www.semi.org/en/about_STMicroelectronics_Smart_Manufacturing_Technology

Use for modern examples of classic SPC methods integrated with fault detection/classification and equipment data.

Source type: industry association / company case-study material.

## 2. Wafer probing and burn-in

### Peter Wolken SEMI oral history

- https://www.semi.org/en/Oral-History-Interview-Peter-Wolken

Use for:

- late-1960s Electroglas automatic wafer prober history;
- equipment-industry and field-service context.

Source type: participant oral history recorded decades later.

Caveat: corroborate priority/“first” claims before using them strongly.

### NASA-TM-X-64686 (1972)

- https://ntrs.nasa.gov/citations/19730007481

Use for:

- qualification;
- power burn-in;
- testing/screening;
- the 100-percent burn-in policy described for the NASA flight-program context covered by the report.

Source type: contemporary government technical memorandum.

### NASA/JPL burn-in guidance

- https://parts.jpl.nasa.gov/asic/Sect.4.3.html

Use for infant-mortality screening and the rationale behind burn-in.

### NASA VLSI reliability / screening constraints

- https://ntrs.nasa.gov/api/citations/19870017771/downloads/19870017771.pdf

Use for caution that conventional burn-in can become expensive or even life-consuming as devices and production contexts change.

Source type: period government reliability study.

## 3. Electromigration

### J. R. Black, 1969

- DOI: 10.1109/PROC.1969.7340
- bibliographic record: https://cir.nii.ac.jp/crid/1362262943933168768

Use for:

- aluminum-metallization wear-out;
- mass transport under electron momentum transfer;
- void/open-circuit failure framing.

Source type: period peer-reviewed technical paper.

Caveat: later copper/barrier/low-k systems have different details. Do not project a single aluminum-era model onto all interconnect generations.

## 4. Solder fatigue and package delamination

### NASA 1969 solder-joint crack study

- https://ntrs.nasa.gov/citations/19690000666

Use for early evidence that PCB/component solder joints were studied under temperature cycling.

Source type: contemporary government engineering report.

### JPL systems approach to solder fatigue (1991)

- https://ntrs.nasa.gov/citations/19930058665

Use for:

- CTE mismatch;
- thermal-cycle strain;
- solder fatigue as packaging-system reliability;
- qualification/testing context.

Source type: JPL/NASA technical paper.

### NASA thermal failure mechanisms

- https://ntrs.nasa.gov/api/citations/20230004376/downloads/20230004376.pdf?attachment=true

Use for modern synthesis of packaging thermal mechanisms including cracking, package defects, CTE mismatch, and delamination.

Source type: modern government reliability handbook/report.

Caveat: not period evidence for when each mechanism was first recognized.

## 5. AOI, ICT, X-ray, and inspectability

### Chin, Harlow, Dwyer — 1979 automatic PCB inspection

- repository record: https://repository.hkust.edu.hk/ir/Record/1783.1-163825
- DOI: 10.1117/12.956747

Use for programmable automatic visual inspection using dimensional verification and pattern matching.

Source type: contemporary conference/research paper.

### Zuech — machine vision in assembled PCB market (2001)

- https://www.automate.org/vision/industry-insights/machine-vision-in-the-assembled-printed-circuit-board-market-part-1

Use for retrospective industry discussion of early-1980s populated-board machine vision / AOI adoption.

Source type: later industry retrospective.

Caveat: do not use as sole support for exact priority claims.

Future primary-source targets:

- early AOI vendor manuals;
- GenRad/Teradyne and other in-circuit-test fixture/tester manuals;
- X-ray inspection equipment literature;
- board-house defect/review procedures;
- operator and rework oral histories.

## 6. 300 mm factory automation, FOUP, GEM, MES, traceability

### SEMI automation history

- https://www.semi.org/en/blogs/the-evolution-of-semiconductor-equipment-automation-standards-from-the-1980s-to-now

Use for:

- SECS-I/SECS-II in the 1980s;
- GEM in the early 1990s;
- transition toward GEM300 with 300 mm manufacturing.

Source type: industry standards-body retrospective.

### SEMI SECS/GEM overview

- https://www.semi.org/en/standards-watch-2022-Sept/intro-to-semi-communication-standards

Use for:

- equipment-host communication;
- 300 mm FOUP transition;
- automatic carrier transport;
- E40/E87/E90/E94 roles.

Source type: industry standards educational material.

### SEMI E47.1 FOUP abstract

- https://store-us.semi.org/products/e04701-semi-e47-1-mechanical-specification-for-foups-used-to-transport-and-store-300-mm-wafers

Use for the explicit purpose of mechanical modularity/interchangeability in 300 mm carrier interfaces.

Source type: standards abstract. The full standard is paywalled.

### SEMI “Gigafab Minute” / MES material

- https://www.semi.org/en/blogs/semi-news/the-gigafab-minute-and-semi-standards-a-modern-miracle

Use for modern description of GEM messaging supporting dispatch, material handling, recipe management, and MES transactions.

Source type: modern SEMI industry explanation.

Caveat: its current-fab quantitative examples should not be projected backward into early GEM deployments.

### SEMI traceability

- https://www.semi.org/en/products-services/standards/traceability

Use for device/substrate identity and end-to-end traceability as an industry standardization problem.

## 7. GDSII, tape-out, and mask-data handoff

### Calma GDS II User's Operating Manual (1978)

- http://www.bitsavers.org/pdf/calma/GDS_II_Users_Operating_Manual_Nov78.pdf

Use for:

- GDS II data structures;
- Stream format;
- hierarchy/structures/references;
- tape-oriented physical record/block behavior.

Source type: primary vendor manual, preserved by Bitsavers.

### Steven M. Rubin, *Computer Aids for VLSI Design*

- https://www.rulabinsky.com/cavd/text/chap07-3.html

Use for later technical explanation of GDSII interchange, compatibility, and hierarchy.

Source type: technical book / secondary source.

### Lynn Conway / Mead–Conway / MOSIS preservation

- https://computerhistory.org/profile/lynn-conway/
- https://computerhistory.org/blog/in-memoriam-lynn-conway-1938-2024/

Use for multi-project-chip service, design-method democratization, and MOSIS lineage.

Source type: Computer History Museum synthesis/profile.

Priority future targets:

- Calma Stream-format manuals/revisions;
- mask-shop job-deck and data-prep manuals;
- e-beam mask-writer manuals;
- MOSIS original service documentation;
- period “tape-out” usage in company/project records.

## 8. Advanced packaging and multi-die systems

### Dataquest/SEMI packaging trends report (1990s)

- https://archive.computerhistory.org/resources/access/text/2013/04/102723374-05-01-acc.pdf

Use for retrospective industry documentation of IBM C4/flip-chip, area-array benefits, and packaging trends.

Source type: industry market/technical report preserved by CHM.

### Ron Gedney oral history

- https://ethw.org/Oral-History%3ARon_Gedney

Use for participant recollection of IBM C4 development and integrated-circuit interconnect challenges.

Source type: participant oral history.

### NASA 2.5D/3D reliability evaluation

- https://ntrs.nasa.gov/citations/20190002150

Use for modern reliability/QA evidence on 2.5D and 3D package configurations.

Source type: government engineering report.

### IBM Research packaging overview

- https://research.ibm.com/blog/what-is-computer-chip-packaging

Use for current corporate description of C4, organic substrates, underfill, high-density interconnection, hybrid-bonding research, and reliability testing.

Source type: corporate research communication.

Caveat: not a neutral history of the entire advanced-packaging industry.

## Cross-cutting preservation rule

This field set is especially vulnerable to source flattening.

Do not treat these as interchangeable:

```text
1969 technical paper
1970s government reliability report
vendor operating manual
industry oral history
standards-body retrospective
modern corporate research blog
museum synthesis
```

They answer different questions.

When a claim concerns exact chronology, process capability, failure rate, or “first,” prefer period documents and independent corroboration.

When a claim concerns why a mature standard exists, standards-body material is valuable but still represents the institution that maintains the standard.

When a claim concerns factory labor or operating practice, actively search for manuals, training documents, photographs, oral histories, and archived procedures — not just inventor biographies.