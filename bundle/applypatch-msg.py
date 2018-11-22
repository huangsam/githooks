#!/usr/bin/env python
import sys

from githooks.core.message import check_message

commit_fl = sys.argv[1]

check_message(commit_fl)
