from dataclasses import dataclass, field


@dataclass
class Object:
    name: str
    owner: str
    readers: set[str] = field(default_factory=set)
    writers: set[str] = field(default_factory=set)

    def can_read(self, user):
        return user == self.owner or user in self.readers or user in self.writers

    def can_write(self, user):
        return user == self.owner or user in self.writers


@dataclass
class Session:
    user: str
    resident_pages: int
    shared_code_pages: int


def fault_domain_demo():
    shared = Object("project-notes", "alice", readers={"bob"}, writers={"carol"})
    for user in ["alice", "bob", "carol", "mallory"]:
        print(
            f"{user:7s} read={str(shared.can_read(user)):5s} "
            f"write={str(shared.can_write(user)):5s}"
        )


def sharing_demo():
    sessions = [
        Session("alice", resident_pages=12, shared_code_pages=8),
        Session("bob", resident_pages=10, shared_code_pages=8),
        Session("carol", resident_pages=14, shared_code_pages=8),
        Session("dave", resident_pages=9, shared_code_pages=8),
    ]

    naive = sum(s.resident_pages + s.shared_code_pages for s in sessions)
    shared_once = sum(s.resident_pages for s in sessions) + max(s.shared_code_pages for s in sessions)

    print("\nSynthetic shared-procedure memory example")
    print(f"private copy for each process: {naive} pages")
    print(f"one shared pure procedure:     {shared_once} pages")
    print(f"pages avoided:                 {naive - shared_once}")


def recovery_demo():
    mtbf_hours = 72.0      # synthetic
    recovery_seconds = 12  # synthetic
    availability = mtbf_hours * 3600 / (mtbf_hours * 3600 + recovery_seconds)
    print("\nSynthetic utility availability")
    print(f"MTBF: {mtbf_hours:.0f} h, recovery: {recovery_seconds} s")
    print(f"availability: {availability * 100:.5f}%")
    print("Parameters are invented; this is not measured Multics availability.")


def main():
    print("Utility-sharing thought experiment")
    fault_domain_demo()
    sharing_demo()
    recovery_demo()


if __name__ == "__main__":
    main()
