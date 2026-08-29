# Why Hybrid Bonding Made Known-Good Die More Valuable

Finer-pitch 3D integration increases bandwidth density, but also raises the cost of discovering a bad die after stacking.

## Historical record

TSMC describes SoIC as integrating known-good dies with sub-10-micrometer-class bond pitch and reports 3 nm chip stacking entering volume production in 2025.[^tsmc]

Intel similarly describes Foveros Direct 3D hybrid bonding and emphasizes multi-stage die sort so faulty dies can be eliminated before packaging.[^intel]

## Engineering reconstruction

A stack yield is a product of multiple independent survival probabilities:

```text
die A good
x die B good
x bonding good
x alignment good
x interface clean
x package good
```

As bond pitch shrinks, inspection, surface preparation, die sorting, wafer mapping, and known-good-die logistics become part of the bandwidth story.

## Speed connection

Hybrid bonding makes more parallel die-to-die wires practical and reduces interconnect parasitics. But if test cannot keep up, the expensive high-bandwidth structure amplifies scrap instead of performance.

## Experiment

`experiments/hybrid-bond-kge/hybrid_bond_kge.py` compares synthetic pre-bond screening strength against assembled-stack yield and test cost.

[^tsmc]: TSMC, “TSMC-SoIC,” https://3dfabric.tsmc.com/chinese/dedicatedFoundry/technology/SoIC.htm
[^intel]: Intel Foundry, “Get the Facts About Intel Foundry,” https://www.intel.com/content/www/us/en/foundry/library/fact-sheet.html
