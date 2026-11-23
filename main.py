#!/usr/bin/env python3
"""Entry for make.fun bounty "news-image-20261123".

The entry image is the file ``entry.png`` shipped in this repository:
a 1024x1024 PNG that sums up the world news of Monday 23 November
2026 in four illustrated panels plus a footer strip. This program
copies it, byte for byte, to ``/output/entry.png``.

It uses only the Python standard library, reaches for no network,
and is fully deterministic: every run writes the same bytes.

Run it locally with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import struct
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
MAX_BYTES = 1_048_576  # the bounty gate: at most 1 MiB
MAX_SIDE = 1024  # the bounty gate: at most 1024 by 1024 pixels
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def png_dimensions(data: bytes) -> tuple[int, int]:
    """Read width/height from a PNG's IHDR chunk (no image library)."""
    if len(data) < 33 or data[12:16] != b"IHDR":
        raise ValueError("not a PNG file")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target = out_dir / "entry.png"

    data = source.read_bytes()
    if data[:8] != PNG_SIGNATURE:
        print("error: entry.png is not a PNG file", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(f"error: entry.png is {len(data)} bytes, over the 1 MiB limit",
              file=sys.stderr)
        return 1
    width, height = png_dimensions(data)
    if width > MAX_SIDE or height > MAX_SIDE:
        print(f"error: entry.png is {width}x{height}, over the 1024x1024 limit",
              file=sys.stderr)
        return 1

    out_dir.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {target} ({width}x{height}, {len(data)} bytes, "
          f"sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
