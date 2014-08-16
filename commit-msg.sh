#!/bin/bash

source "${GIT_DIR}/hooks/verify"

verify_non_master
verify_commit "$1"
