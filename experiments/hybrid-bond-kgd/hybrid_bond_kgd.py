print('Synthetic known-good-die / stack-yield model')
die_yield = 0.93
bond_yield = 0.985
for screening in (0.80, 0.95, 0.995):
    accepted_good = die_yield * screening
    accepted_bad = (1 - die_yield) * (1 - screening)
    incoming_quality = accepted_good / (accepted_good + accepted_bad)
    stack_yield = (incoming_quality ** 2) * bond_yield
    test_cost_proxy = 1.0 + 2.0 * screening
    print(f'screen={screening:.3f} incoming_quality={incoming_quality:.4f} stack_yield={stack_yield:.4f} test_cost={test_cost_proxy:.2f}')
print('Synthetic model; not a hybrid-bond manufacturing forecast.')
