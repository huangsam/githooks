#!/bin/bash

verify_commit() {
    COMMIT_FL=$1

    python "${GIT_DIR}/hooks/check_msg" "${COMMIT_FL}"

    if [ $? -ne 0 ] ; then
        exit 190
    fi
}

verify_flake8() {
    which flake8 &> /dev/null

    if [ $? -ne 0 ] ; then
        echo '[POLICY] Install Flake8 package before commit'
        exit 191
    fi

    BAD=0

    for pyfl in $(git diff --cached --name-only --diff-filter=ACMR \
        | egrep '.py$') ; do
        flake8 --show-source "${pyfl}"
        let "BAD|=$?"
    done

    if [ ${BAD} -ne 0 ] ; then
        echo '[POLICY] Fix Flake8 error(s) before commit'
        exit 192
    fi
}

verify_non_master() {
    git log >& /dev/null || exit 0

    CURRENT=$(git rev-parse --abbrev-ref HEAD)

    if [ "${CURRENT}" == 'master' ] ; then
        echo '[POLICY] Never commit directly to master'
        exit 193
    fi
}

verify_no_conflict() {
    COMMIT_FL=$1

    grep -i 'Conflicts' "${COMMIT_FL}" > /dev/null
    if [ $? -eq 0 ] ; then
        echo '[POLICY] Never commit merge conflicts'
        exit 194
    fi
}
