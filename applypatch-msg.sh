#!/bin/bash

source "${GIT_DIR}/hooks/commons"

verify_non_master
verify_commit "$1"
