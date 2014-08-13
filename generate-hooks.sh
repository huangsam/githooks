#!/bin/bash

# generate hooks directory

mkdir -p hooks

# move script(s) into hooks directory

for fl in `ls | egrep '(.py|.sh)$' | egrep -v $0` ; do
    tmp_fl=${fl%.py}
    new_fl=${tmp_fl%.sh}
    cp ${fl} hooks/${new_fl}
    chmod 744 hooks/${new_fl}
done
