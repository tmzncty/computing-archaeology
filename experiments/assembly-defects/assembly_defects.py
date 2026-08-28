#!/usr/bin/env python3
"""Synthetic comparison of assembly defect structures."""

CONNECTIONS = [50, 200, 1000]
HAND_DEFECT = 0.002      # synthetic per connection
PCB_JOINT_DEFECT = 0.0005
PCB_PROCESS_DEFECT = 0.01  # synthetic board-wide process loss


def independent_success(n: int, p: float) -> float:
    return (1.0 - p) ** n


def main() -> None:
    print("Synthetic assembly defect model\n")
    print("connections  hand-wired success  PCB/batch-process success")
    for n in CONNECTIONS:
        hand = independent_success(n, HAND_DEFECT)
        pcb = (1.0 - PCB_PROCESS_DEFECT) * independent_success(n, PCB_JOINT_DEFECT)
        print(f"{n:11d}  {hand:18.2%}  {pcb:25.2%}")
    print("\nProbabilities are invented; compare failure structures, not historical rates.")


if __name__ == "__main__":
    main()
