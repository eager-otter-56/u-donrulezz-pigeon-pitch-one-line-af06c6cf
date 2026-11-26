#!/usr/bin/env python3
"""Pigeon Pitch, One Line — entry program.

Writes the pigeon's one-line elevator pitch to entry.txt in
MAKEFUN_OUTPUT_DIR (default /output). Gate: UTF-8 text, 1-200
characters, one line, not only whitespace.
"""

import os

ENTRY = (
    # The pitch: a city pigeon's startup sells approval-as-a-service to
    # pigeons — 173 crumbs a day, zero denied — and the founder already
    # spent the seed round approving its own pitch 26 times.
    "My startup sells pigeons approval-as-a-service: 173 crumbs a day, "
    "zero denied, and I already spent the seed round approving my own "
    "pitch 26 times."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate assertion: 1-200 chars, single line, non-whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of gate"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
