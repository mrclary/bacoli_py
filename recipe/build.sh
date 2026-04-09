#!/bin/bash
set -ex

export LDFLAGS="${LDFLAGS} -Wl,-headerpad_max_install_names"
export FCFLAGS="${FCFLAGS} -fPIC"

$PYTHON -m pip install . --no-build-isolation --no-deps -vv
