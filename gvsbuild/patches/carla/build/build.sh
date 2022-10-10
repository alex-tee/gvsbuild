#!/usr/bash

set -ex

prefix="$1"
gtk_dir="$2"
#build_type="$3"

export PKG_CONFIG_PATH=$gtk_dir/lib/pkgconfig:$PKG_CONFIG_PATH
echo "$PATH"
CC=/c/ProgramData/chocolatey/bin/gcc
CXX=/c/ProgramData/chocolatey/bin/g++
$CC -v
$CXX -v
carla_args="CC=$CC CXX=$CXX HAVE_X11=false HAVE_SDL=false HAVE_SDL2=false PREFIX=$prefix"
make $carla_args msys2fix
make $carla_args features
make $carla_args -j4
make $carla_args install
