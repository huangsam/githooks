#!/bin/bash
set -eu

for fl in bundle/*; do
    name="$(basename $fl)"
    path=".git/hooks/${name%.py}"
    cp "$fl" "$path"
    chmod +x "$path"
done
