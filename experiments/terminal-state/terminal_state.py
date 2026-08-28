ESC = "\x1b"


class TinyTerminal:
    def __init__(self, rows=6, cols=30):
        self.rows = rows
        self.cols = cols
        self.screen = [[" " for _ in range(cols)] for _ in range(rows)]
        self.row = 0
        self.col = 0

    def put(self, ch):
        if ch == "\r":
            self.col = 0
        elif ch == "\n":
            self.row = min(self.rows - 1, self.row + 1)
        elif ch.isprintable():
            self.screen[self.row][self.col] = ch
            self.col += 1
            if self.col >= self.cols:
                self.col = 0
                self.row = min(self.rows - 1, self.row + 1)

    def csi(self, params, final):
        if final == "H":
            parts = [int(p) if p else 1 for p in params.split(";")]
            row = parts[0] if parts else 1
            col = parts[1] if len(parts) > 1 else 1
            self.row = max(0, min(self.rows - 1, row - 1))
            self.col = max(0, min(self.cols - 1, col - 1))
        elif final == "J" and params in ("2", ""):
            self.screen = [[" " for _ in range(self.cols)] for _ in range(self.rows)]
            self.row = 0
            self.col = 0

    def feed(self, data):
        i = 0
        while i < len(data):
            if data.startswith(ESC + "[", i):
                j = i + 2
                while j < len(data) and (data[j].isdigit() or data[j] == ";"):
                    j += 1
                if j < len(data):
                    self.csi(data[i + 2:j], data[j])
                    i = j + 1
                    continue
            self.put(data[i])
            i += 1

    def render(self):
        return "\n".join("".join(row) for row in self.screen)


def main():
    term = TinyTerminal()

    full_repaint = (ESC + "[2J" +
                    "SYSTEM STATUS\r\n" +
                    "CPU: OK\r\n" +
                    "DISK: OK\r\n" +
                    "USERS: 12\r\n")
    term.feed(full_repaint)
    print("Initial terminal state:\n")
    print(term.render())

    update = ESC + "[4;8H" + "13"
    term.feed(update)

    print("\nAfter stateful cursor update:\n")
    print(term.render())
    print("\nByte counts")
    print(f"initial repaint: {len(full_repaint.encode())}")
    print(f"small update:    {len(update.encode())}")
    print()
    print("This parser supports only a tiny pedagogical subset of ANSI/VT100-style behavior.")


if __name__ == "__main__":
    main()
