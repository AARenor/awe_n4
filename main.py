"""make.fun entry for the bounty "Make the AI judge feel awe".

This program copies the short relaxing text in entry.txt, which sits beside it,
byte for byte into MAKEFUN_OUTPUT_DIR (default /output) as entry.txt. It adds
nothing: no newline, no header, no fallback text. A missing source file raises.

Python 3.13 standard library only. No network, no arguments.
"""

import os
from pathlib import Path


def entry_path() -> Path:
    """Return the text to hand in, read from beside this program."""
    return Path(__file__).resolve().parent / "entry.txt"


def output_path() -> Path:
    """Return the file the sandbox gate reads, under MAKEFUN_OUTPUT_DIR."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def main() -> None:
    """Copy the entry text out unchanged, raising if there is none to copy."""
    source = entry_path()
    if not source.is_file():
        raise FileNotFoundError(f"entry text is missing: {source}")

    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(source.read_bytes())


if __name__ == "__main__":
    main()
