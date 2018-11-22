#!/usr/bin/env python
import sys

from githooks.core.message import check_message
from githooks.core.branch import check_non_master

commit_fl = sys.argv[1]

check_non_master()
check_message(commit_fl)
