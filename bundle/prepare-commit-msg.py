#!/usr/bin/env python
import fileinput
import sys

from githooks.core.branch import check_no_conflict
from githooks.utils.git import branch_tag

commit_fl: str = sys.argv[1]

source: str | None

try:
    source = sys.argv[2]
except IndexError:
    source = None


def replace_with_tag(commit_fl: str) -> None:
    tag = branch_tag().upper()
    with fileinput.FileInput(commit_fl, inplace=True) as f:
        for line in f:
            print(line.replace("COMMIT-TAG", tag), end="")


if source == "message":
    replace_with_tag(commit_fl)
elif source == "merge":
    check_no_conflict(commit_fl)
    replace_with_tag(commit_fl)
elif source == "template":
    replace_with_tag(commit_fl)
