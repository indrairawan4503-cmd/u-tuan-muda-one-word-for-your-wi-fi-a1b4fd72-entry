#!/usr/bin/env python3
"""One Word for Your Wi-Fi entry (variant A): "Houdini".

The Wi-Fi pulls a Houdini - it vanishes exactly when you need it most.
Writes the word to /output/entry.txt FIRST, then a byte-identical copy
to entry.txt in the repo root (guarded: the grader sandbox mounts the
repo read-only, so a failed copy must never crash the run).
Deterministic: no randomness, no network.
"""

import os

WORD = "Houdini"


def write_repo_copy(data: str) -> None:
    """Best-effort byte-identical copy next to main.py.

    The grader sandbox mounts the repo read-only, so a failed copy
    must never crash the run.
    """
    try:
        with open(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"),
            "w",
            encoding="utf-8",
        ) as f:
            f.write(data)
    except OSError:
        pass


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    write_repo_copy(WORD)


if __name__ == "__main__":
    main()
