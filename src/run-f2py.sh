#!/bin/bash
set -e

# This script is required because f2py will only save the output compiled
# file to the current directory, but meson expects it to be in src

python="$1"
out_dir="$(dirname "$2")"
out_file="$(basename "$2")"

set -x

"$python" -m numpy.f2py --backend meson -m bacoli_interface -c ${@:3}

mv $out_file "$out_dir"
