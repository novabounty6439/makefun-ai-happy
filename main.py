#!/usr/bin/env python3
"""make.fun ai-happy-01 entry: write the happiest picture to /output/entry.png.

The program copies the bundled AI-generated photo of a joyful golden
retriever puppy leaping through a sunny wildflower meadow to the output
path. The copy is byte-for-byte deterministic: two runs always produce
identical bytes, and no network access is needed.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "happy.jpg"


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"Source image not found: {SOURCE}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.png"
    shutil.copyfile(SOURCE, out_path)
    # Verify the copy is complete: sizes must match exactly.
    if out_path.stat().st_size != SOURCE.stat().st_size:
        raise SystemExit(f"Copy incomplete: {out_path} size mismatch")
    print(f"Wrote {out_path} ({out_path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
