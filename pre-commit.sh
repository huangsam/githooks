#!/bin/bash

source ${GIT_DIR}/hooks/verify

verify_flake8
verify_non_master
