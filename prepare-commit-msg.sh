#!/bin/bash

source "${GIT_DIR}/hooks/verify"

function replace_tag() {
    git log >& /dev/null
    if [ $? -ne 0 ] ; then
        return
    fi

    # utilize branch prefix as commit-tag for message
    CURRENT=$(git rev-parse --abbrev-ref HEAD)
    CBRANCH=$(echo "${CURRENT}" | awk -F '/' '{print $1}' | tr '[:lower:]' '[:upper:]')
    sed -ie "s/COMMIT-TAG/${CBRANCH}/g" "$1"
}

# resolve commit, merge, message, squash and template

case ":$2" in
    :commit|:message|:squash)
        verify_commit "$1"
        replace_tag "$1" ;;

    :merge)
        verify_no_conflict "$1"
        replace_tag "$1" ;;

    :template)
        replace_tag "$1" ;;
esac
