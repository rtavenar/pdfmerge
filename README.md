# `pdfmerge`: a simple command-line tool to merge PDF files

```bash
$python -m pip install pypdf2
[...]
$ python pdfmerge.py -h
usage: pdfmerge.py [-h] [--output OUTPUT] input_files [input_files ...]

Concatenate PDF files.

positional arguments:
  input_files      Input PDF files to concatenate

optional arguments:
  -h, --help       show this help message and exit
  --output OUTPUT  Output file name (default: "merged.pdf")
```
