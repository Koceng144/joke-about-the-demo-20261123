#!/usr/bin/env python3
"""Entry for the-joke-about-the-demo-20261123-0112.

Writes one fixed one-line joke to /output/entry.txt: a joke about
working alongside AI coding agents, and a demo that crashes. No
network, standard library only.
"""

import os
import sys

TEXT = (
    "The demo crashed, the room applauded, and my agent took a bow "
    "— it thought the error page was the feature I'd asked for."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    out_dir = os.path.dirname(OUTPUT_PATH)
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(TEXT)
            fh.flush()
            os.fsync(fh.fileno())  # the scorer reads the file after exit
    except OSError:
        # Fall back to the current directory if /output is not writable.
        try:
            with open("entry.txt", "w", encoding="utf-8", newline="\n") as fh:
                fh.write(TEXT)
        except OSError:
            pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
