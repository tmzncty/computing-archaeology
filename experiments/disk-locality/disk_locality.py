import random

TRACKS = 200
RECORDS_PER_TRACK = 20
SEEK_PER_TRACK_MS = 2.5       # synthetic
FULL_ROTATION_MS = 50.0       # synthetic
TRANSFER_PER_RECORD_MS = 0.15 # synthetic


def access_cost(previous_track, track, rotational_fraction):
    seek = abs(track - previous_track) * SEEK_PER_TRACK_MS
    rotation = rotational_fraction * FULL_ROTATION_MS
    return seek + rotation + TRANSFER_PER_RECORD_MS


def run_workload(records):
    previous_track = 0
    total = 0.0
    for record in records:
        track = record // RECORDS_PER_TRACK
        rotational_fraction = (record % RECORDS_PER_TRACK) / RECORDS_PER_TRACK
        total += access_cost(previous_track, track, rotational_fraction)
        previous_track = track
    return total


def main():
    random.seed(305)
    sample = random.sample(range(TRACKS * RECORDS_PER_TRACK), 80)
    random_order = sample[:]
    clustered_order = sorted(sample)

    random_cost = run_workload(random_order)
    clustered_cost = run_workload(clustered_order)

    sequential = list(range(1000, 1080))
    sequential_cost = run_workload(sequential)

    print("Synthetic moving-head disk locality model")
    print(f"records requested:        {len(sample)}")
    print(f"random-order cost:        {random_cost:8.1f} ms")
    print(f"same records, clustered: {clustered_cost:8.1f} ms")
    print(f"sequential run:           {sequential_cost:8.1f} ms")
    print()
    print("All timing constants are invented teaching parameters.")
    print("The experiment demonstrates geometry/locality, not IBM 350 timing.")


if __name__ == "__main__":
    main()
