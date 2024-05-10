#!/bin/bash
if [ -z "$READTHEDOCS" ]; then
  echo "Can only run this script on Read the Docs"
  exit 1
fi

version=$(sed -n '3p' docs/report/019/Manifest.toml | cut -d'"' -f2)
major_version=${version:0:-2}
echo "Installing Julia v${version}"
filename=julia-${version}-linux-x86_64.tar.gz
wget -q https://julialang-s3.julialang.org/bin/linux/x64/${major_version}/${filename}
tar xzf ${filename} -C ~/.asdf --strip-components=1
