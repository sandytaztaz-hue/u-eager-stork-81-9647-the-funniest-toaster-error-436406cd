#!/usr/bin/env python3
"""Entry program: writes the funniest toaster error message to /output/entry.txt.

The line is a deadpan status report from a small appliance that has
simply decided not to toast: lever down, bread in, refusal last.
"""

import os

ENTRY = "Lever down. Bread in. I have decided not to."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
