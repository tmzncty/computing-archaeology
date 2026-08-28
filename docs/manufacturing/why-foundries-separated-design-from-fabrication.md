# Why Foundries Separated Design from Fabrication

For much of semiconductor history, a chip company was expected to design the device **and** own the factory that manufactured it.

That model tied product design, process engineering, capital investment, yield learning, and production scheduling inside one firm.

The historical question is:

> **What changes when manufacturing becomes a service that independent design companies can buy?**

The foundry model changes not only corporate structure but the kinds of semiconductor companies that can exist.

## The integrated device manufacturer was the default

Bell Labs, Fairchild, Texas Instruments, Intel, Motorola, IBM, and many other early semiconductor organizations combined large amounts of product and process knowledge internally.

This made sense because process technology was deeply entangled with device design.

A company building a new transistor or IC often had to develop:

```text
materials
process recipe
equipment modifications
layout rules
test methods
package
product design
```

The factory was therefore part of the design organization.

## Rising fab cost changes the boundary of the firm

As wafer size, process complexity, equipment specialization, and cleanroom requirements increased, a competitive fab required more capital and more specialized process engineering.

At the same time, design expertise could become valuable independently of factory ownership.

This creates a structural possibility:

```text
design company
-> sends manufacturable design
-> independent foundry
-> returns tested wafers / die
```

The business boundary can move because interfaces between design and manufacturing become formal enough to support it.

## The interface must become explicit

A foundry relationship requires more than a purchase order.

The design customer needs to know what the process can manufacture.

That means the manufacturing process must be represented through artifacts such as:

- design rules;
- device models;
- layer definitions;
- mask-data conventions;
- electrical limits;
- test structures;
- package options;
- qualification requirements.

### Reconstruction

This is an important abstraction transition.

An internal fab can sometimes rely on informal coordination between process engineers and circuit designers.

A foundry serving many outside customers must turn much more of that tacit knowledge into an **interface contract**.

The manufacturing process becomes programmable in a limited but powerful sense: designers work inside a published process envelope.

## TSMC formalizes the pure-play foundry model

Taiwan Semiconductor Manufacturing Company was founded in 1987 and describes itself as the pioneer of the pure-play foundry business model: manufacturing customers' semiconductor products while not competing with them through its own branded semiconductor products.[^tsmc-profile]

A 1997 TSMC annual-report page described the company as the first pure IC foundry and emphasized the idea that the foundry should be a partner rather than a product competitor.[^tsmc-1997]

This is corporate self-description and should be treated as such, but it documents the business model the company deliberately presented to customers and investors.

## Fabless companies become structurally easier to create

Once a capable external foundry exists, a semiconductor startup no longer needs to finance a complete advanced wafer fab before selling its first product.

It still needs substantial engineering capability:

```text
architecture
logic / circuit design
physical design
verification
foundry interface
packaging / test strategy
product engineering
```

But one enormous fixed-cost layer can be purchased as manufacturing service.

TSMC's later annual reports explicitly connect the foundry model with the rise of the fabless semiconductor industry.[^tsmc-2021]

## Manufacturing does not become generic

The foundry model can be misunderstood as:

> design is universal; the fab merely prints it.

That is false.

Design and manufacturing remain coupled through:

- process-specific design rules;
- timing and device models;
- allowed voltages;
- memory/compiler macros;
- analog device options;
- metal-stack choices;
- yield-sensitive geometries;
- package and test constraints.

The relationship changes from ownership to **contracted co-design**.

Modern foundry ecosystems reinforce this with process design kits, reference flows, EDA partnerships, and IP libraries.

TSMC itself has described manufacturing readiness as something that increasingly has to exist inside the design environment, not only on the factory floor.[^tsmc-collab]

## Foundries change innovation geography

A fabless company can be geographically distant from the wafer fab.

That allows semiconductor product design to cluster around different labor markets, universities, customers, and software ecosystems than fabrication.

At the same time, manufacturing knowledge, equipment supply chains, materials, packaging, and logistics become concentrated in their own regions.

The semiconductor industry becomes more modular — and more interdependent.

## The split creates new failure modes

Separation also adds coordination problems:

- design-rule interpretation;
- model accuracy;
- mask-data handoff;
- process revisions;
- yield ownership;
- test correlation;
- capacity allocation;
- supply-chain risk.

The integrated firm can resolve some of these through internal authority.

A foundry ecosystem needs formal interfaces, contracts, standards, and shared engineering tools.

## Why this belongs in computing history

The rise of fabless design companies changes which computing products are economically possible.

A GPU startup, network-chip company, storage-controller vendor, or custom-accelerator firm can exist without first becoming a full semiconductor manufacturer.

That means corporate structure becomes an architectural enabling condition.

The history of modern processors is therefore also a history of:

> **manufacturing becoming an external platform.**

## What this teaches us

The foundry model does not remove manufacturing from chip design.

It changes how manufacturing constraints are communicated.

What used to be embodied partly in one company's internal process organization becomes a formal boundary of:

```text
PDK
models
design rules
mask data
test
qualification
capacity
```

The fab becomes a service platform, and that organizational innovation helps create the modern fabless semiconductor ecosystem.

## References

[^tsmc-profile]: Taiwan Semiconductor Manufacturing Company, company profile, https://www.tsmc.com/english/aboutTSMC/company_profile
[^tsmc-1997]: TSMC, 1997 Annual Report, “Company Profile,” https://investor.tsmc.com/static/annualReports/1997/company1.html
[^tsmc-2021]: TSMC, 2021 Annual Report, “About TSMC,” https://investor.tsmc.com/static/annualReports/2021/english/index.html
[^tsmc-collab]: TSMC, “TSMC Says IC Industry Success Starts with Design Collaboration,” 2004, https://pr.tsmc.com/english/news/1287

## Source note

TSMC sources are corporate self-descriptions. They are appropriate for documenting TSMC's stated business model, dates, and ecosystem framing but should be corroborated with independent scholarship for priority, industrial impact, state policy, technology transfer, and the broader emergence of foundry/fabless structures.