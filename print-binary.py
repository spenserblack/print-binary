#!/usr/bin/env python3
import sys
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser, FileType

BINARY = 2
OCTAL = 8
DECIMAL = 10
HEX = 16
CHARS_PER_BYTE = {
    BINARY: 8,
    OCTAL: 3,
    DECIMAL: 3,
    HEX: 2,
}

parser = ArgumentParser(
    description="Write a binary file", formatter_class=ArgumentDefaultsHelpFormatter
)
parser.add_argument(
    "-i",
    "--input",
    metavar="FILE",
    type=FileType("r"),
    default="-",
    help="A file to read from (- is STDIN)",
)
parser.add_argument(
    "-m",
    "--mode",
    metavar="N",
    type=int,
    choices=[BINARY, OCTAL, DECIMAL, HEX],
    default=BINARY,
    help="Interpret the text as base-N",
)

args = parser.parse_args()
base = args.mode

while True:
    chars = args.input.read(CHARS_PER_BYTE[base]).strip()  # NOTE Remove whitespace
    if not chars:
        break
    byte = int(chars, base=base).to_bytes(1, sys.byteorder)
    sys.stdout.buffer.write(byte)
