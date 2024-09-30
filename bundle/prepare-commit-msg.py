#!/usr/bin/env python
import sys

from githooks.core.branch import check_no_conflict
from githooks.utils.git import branch_tag

commit_fl: str = sys.argv[1]

source: str | None

try:
    source = sys.argv[2]
except IndexError:
    source = None


_content = """
[COMMIT-TAG] Enter summary in 50 characters or less

# Enter explanatory text, if necessary. The maximum length of
# each line is 72 characters
#
# Add extra paragraphs as necessary with line breaks in between
#
#     - Use indented hyphens for bullet points
#
# METADATA-LABEL: ID
""".strip()


if source is None:
    tag = f"[{branch_tag().upper()}]"
    _content = _content.replace("COMMIT-TAG", tag)
    print(_content)

elif source == "merge":
    check_no_conflict(commit_fl)
