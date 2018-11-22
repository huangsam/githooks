#!/usr/bin/env python
import sys

from githooks.core.branch import check_non_master
from githooks.core.message import check_message

check_non_master()
check_message(sys.argv[1])
