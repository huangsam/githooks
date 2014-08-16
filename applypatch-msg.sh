#!/bin/bash

source "${GIT_DIR}/hooks/verify"

verify_commit "$1"
