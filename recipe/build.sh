#!/bin/bash
set -ex

# export CC=/opt/homebrew/bin/gcc-15
# export CXX=/opt/homebrew/bin/g++-15
# export FC=/opt/homebrew/bin/gfortran
# export F77=$FC

# export LDFLAGS="${LDFLAGS} -Wl,-headerpad_max_install_names"
# export FCFLAGS="${FCFLAGS} -fPIC"

# $PYTHON -m pip install . --no-build-isolation --no-deps -vv
$PYTHON -m pip install --no-deps -vv dist/bacoli*.whl
