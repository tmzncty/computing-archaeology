"""Synthetic fixed-ROM versus EPROM-style development-loop model."""

ITERATIONS = 10
FIXED_ROM_TURN_HOURS = 72
EPROM_ERASE_PROGRAM_TEST_HOURS = 1.5

fixed = ITERATIONS * FIXED_ROM_TURN_HOURS
eprom = ITERATIONS * EPROM_ERASE_PROGRAM_TEST_HOURS

print(f"{ITERATIONS} synthetic fixed-ROM iterations: {fixed:.1f} h")
print(f"{ITERATIONS} synthetic EPROM-style iterations: {eprom:.1f} h")
print(f"feedback-loop ratio: {fixed/eprom:.1f}x")