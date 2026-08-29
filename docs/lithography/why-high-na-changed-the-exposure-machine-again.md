# Why High-NA Changed the Exposure Machine Again

EUV did not end lithography scaling. The next lever was numerical aperture.

ASML's High-NA EXE platform raises NA from 0.33 to 0.55. ASML states that the first High-NA system was delivered in December 2023 and positions the platform for process development and later high-volume manufacturing.[^asml]

## Engineering reconstruction

A simplified resolution relation is often written as:

```text
resolution ~ k1 * wavelength / NA
```

At fixed wavelength, higher NA can resolve smaller features. But NA is not a free number.

Increasing it changes:

- mirror geometry;
- depth-of-focus budget;
- reticle/wafer imaging strategy;
- stage speed and synchronization;
- aberration control;
- metrology;
- resist/process windows;
- tool size, mass, service, and capital intensity.

## The machine gets larger as the pattern gets smaller

This is one of the central ironies of modern manufacturing. The printed feature shrinks while the machine required to print it grows in optical, mechanical, vacuum, control, and logistics complexity.

High-NA therefore belongs in computing history not as a spec-sheet improvement, but as evidence that geometric scaling increasingly depends on system-level precision infrastructure.

## Experiment

[`experiments/highna-field/highna_field.py`](../../experiments/highna-field/highna_field.py) uses a synthetic wavelength/NA resolution proxy and adds a field/stage burden term. It demonstrates that improved nominal resolution can coexist with increased machine/process burden.

## Source caution

ASML's stated 0.55 NA and platform shipment chronology describe its own system roadmap. Production-node timing can shift and must be dated precisely when discussed.

[^asml]: ASML, “EUV lithography systems,” https://www.asml.com/en/en/products/euv-lithography-systems
