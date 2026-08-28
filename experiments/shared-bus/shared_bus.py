from collections import deque
from dataclasses import dataclass


@dataclass
class Request:
    source: str
    words: int
    priority: int


def fixed_priority_schedule(requests, bus_words_per_tick=8):
    queues = {}
    for req in requests:
        queues.setdefault(req.priority, deque()).append(req)

    ticks = 0
    transfers = {"CPU": 0, "DISK": 0, "NET": 0}
    order = []

    while any(queues.values()):
        priority = max(p for p, q in queues.items() if q)
        req = queues[priority][0]
        moved = min(bus_words_per_tick, req.words)
        req.words -= moved
        transfers[req.source] += moved
        order.append(req.source)
        ticks += 1
        if req.words == 0:
            queues[priority].popleft()

    return ticks, transfers, order


def cpu_mediated_io(disk_words, net_words):
    # Synthetic model: each device word consumes two bus movements:
    # device -> CPU and CPU -> memory.
    return 2 * (disk_words + net_words)


def dma_io(disk_words, net_words):
    # Synthetic model: device -> memory directly.
    return disk_words + net_words


def main():
    disk_words = 256
    net_words = 96

    print("Shared-bus / DMA thought experiment")
    print(f"CPU-mediated I/O bus-word movements: {cpu_mediated_io(disk_words, net_words)}")
    print(f"DMA-style bus-word movements:         {dma_io(disk_words, net_words)}")
    print()

    requests = [
        Request("CPU", 96, 1),
        Request("DISK", 256, 3),
        Request("NET", 96, 2),
        Request("CPU", 128, 1),
    ]
    ticks, transfers, order = fixed_priority_schedule(requests)
    print(f"synthetic arbitration ticks: {ticks}")
    print("transferred words:")
    for source, words in transfers.items():
        print(f"  {source:4s}: {words}")
    print("first 20 bus owners:", " ".join(order[:20]))
    print()
    print("Priorities and transfer width are invented teaching parameters.")
    print("This exposes shared ownership/contention; it is not UNIBUS timing.")


if __name__ == "__main__":
    main()
