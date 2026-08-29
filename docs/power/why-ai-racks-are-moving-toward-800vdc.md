# Why AI Racks Are Moving Toward 800 VDC

Rack power grew until current itself became a scaling problem.

## Historical record

In August 2026, Google, Microsoft, and NVIDIA described work inside the Open Compute Project to standardize 800 VDC distribution for next-generation AI datacenters. The stated motivation is to move more power with less conductor/copper than lower-voltage alternatives.[^ocp]

## Engineering reconstruction

For the same power:

```text
current = power / voltage
```

Raising distribution voltage reduces current. Lower current can reduce conductor cross-section, I-squared-R loss, connector heating, and busbar bulk, although it raises insulation, clearance, conversion, protection, safety, and fault-energy requirements.

## Speed connection

A rack that cannot receive stable power cannot sustain accelerator clocks. Power conversion and distribution latency are not instruction latency, but they set the envelope in which fast compute can operate continuously.

## Experiment

`experiments/hvdc-rack-current/hvdc_rack_current.py` compares synthetic rack currents and copper-loss proxies at several distribution voltages.

[^ocp]: Open Compute Project, “Powering the Next Era of AI ... Transition to LVDC,” 2026, https://www.opencompute.org/index.php/blog/powering-the-next-era-of-ai-how-google-microsoft-and-nvidia-are-standardizing-and-accelerating-the-industry-transition-to-lvdc
