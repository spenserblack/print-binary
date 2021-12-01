# print-binary

A helper script I use to convert a string of bytes as binary, octal, etc. to binary that
I might write to a file.

## Basic Usage

```bash
# reads hexadecimal 40 (64 in decimal) as a byte and writes it
printf 40 | print-binary.py --mode 16
# prints @
```
