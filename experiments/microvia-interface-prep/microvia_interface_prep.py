"""Synthetic laser-microvia cleaning/seed-continuity model."""


def reliability(laser_residue, clean_strength, surface_damage):
    residue_left = max(0.0, laser_residue * (1.0 - clean_strength))
    damage = surface_damage * clean_strength**2
    seed_continuity = max(0.0, 1.0 - 0.8 * residue_left - 0.7 * damage)
    final = seed_continuity * (1.0 - 0.4 * damage)
    return residue_left, damage, seed_continuity, max(0.0, final)


def main():
    residue = 0.8
    surface_damage = 0.5
    for clean in (0.1, 0.3, 0.5, 0.7, 0.9, 1.0):
        r, d, seed, final = reliability(residue, clean, surface_damage)
        print(
            f"clean={clean:3.1f} residue={r:5.3f} damage={d:5.3f} "
            f"seed={seed:5.3f} final_proxy={final:5.3f}"
        )


if __name__ == "__main__":
    main()
