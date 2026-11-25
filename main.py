#!/usr/bin/env python3
"""Monday Morning Punchlines — one original joke about Monday mornings.

The joke lives in the JOKE constant below. The program validates it
(1-200 characters, valid UTF-8, not only whitespace) and writes it to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``), then verifies the
write with a round-trip byte check.
"""

import os
import sys

JOKE = "I asked Monday for a day off. It laughed, then booked a meeting to discuss my attitude."

MAX_CHARS = 200


def validate(text: str) -> None:
    """Raise ValueError unless *text* is a usable joke."""
    if not isinstance(text, str):
        raise ValueError("joke must be a string")
    if not text.strip():
        raise ValueError("joke must not be only whitespace")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "joke must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if any(ord(ch) < 0x20 and ch not in "\t" for ch in text):
        raise ValueError("joke must not contain control characters")
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8


def main() -> int:
    validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = JOKE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Round-trip check: what landed on disk must be exactly the joke.
    # Bytes must match, and decoding them must reproduce the joke and
    # pass validation again — a truncated or mangled write fails here.
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise RuntimeError("round-trip check failed: entry.txt bytes differ from joke")
    validate(written.decode("utf-8"))
    if written.decode("utf-8") != JOKE:
        raise RuntimeError("round-trip check failed: decoded entry.txt differs from joke")
    print("Wrote %d bytes (%d chars) to %s" % (len(data), len(JOKE), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
