#!/bin/bash

source ${GIT_DIR}/hooks/verify

CURRENT=`git rev-parse --abbrev-ref HEAD`

# utilize branch prefix as commit-tag for message

CBRANCH=`echo ${CURRENT} | awk -F '/' '{print $1}' | tr '[a-z]' '[A-Z]'`

# resolve commit, merge, message, squash and template

case ":$2" in
    :commit|:message|:squash)
        verify_commit $1
        sed -ie "s/COMMIT-TAG/${CBRANCH}/g" $1 ;;

    :merge)
        verify_no_conflict $1
        sed -ie "s/COMMIT-TAG/${CBRANCH}/g" $1 ;;

    :template)
        sed -ie "s/COMMIT-TAG/${CBRANCH}/g" $1 ;;
esac
