#!/bin/bash

set -e

rm -rf _build
d2lbook build html
python3 tools/format_tables.py

python3 -m http.server --directory ./_build/html/
