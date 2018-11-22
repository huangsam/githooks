#!/usr/bin/env python
import sys

from githooks.core.message import check_message, check_non_master

commit_fl = sys.argv[1]

check_non_master()
check_message(commit_fl)
