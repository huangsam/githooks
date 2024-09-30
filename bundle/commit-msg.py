#!/usr/bin/env python3
import sys

from githooks.core.branch import check_no_trunk
from githooks.core.message import check_message

commit_fl: str = sys.argv[1]

check_no_trunk()
check_message(commit_fl)
