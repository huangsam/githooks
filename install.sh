#!/bin/bash

BASE_DIR=$(pwd)
SCRIPT_DIR="${BASE_DIR}/githooks/"
GIT_DIR="${BASE_DIR}/.git/hooks"

FL_NAME=$(basename "$0")

# install hooks and supporting scripts
for fl in $(find "${SCRIPT_DIR}" -type f -depth 1 \
    | egrep '(.py|.sh)$' \
    | egrep -v "$FL_NAME" \
    | xargs basename) ; do

    tmp_fl=${fl%.py}
    new_fl=${tmp_fl%.sh}

    if [ -f "${GIT_DIR}/${new_fl}" ]; then
        mv "${GIT_DIR}/${new_fl}" "${GIT_DIR}/${new_fl}.bak"
    fi

    cp "${SCRIPT_DIR}/${fl}" "${GIT_DIR}/${new_fl}"
    chmod 744 "${GIT_DIR}/${new_fl}"

done

# install commit message template in local config
cp "${SCRIPT_DIR}git-commit-template.txt" "${GIT_DIR}/git-commit-template.txt"
git config --local commit.template "${GIT_DIR}/git-commit-template.txt"

