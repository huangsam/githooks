#!/usr/bin/env python3
import sys

from githooks.core.branch import check_no_conflict
from githooks.utils.git import branch_tag

commit_fl: str = sys.argv[1]

source: str | None

try:
    source = sys.argv[2]
except IndexError:
    source = None

template = """
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
    with open(commit_fl, "w") as f:
        tag = branch_tag().upper()
        content = template.replace("COMMIT-TAG", tag)
        f.write(content)

elif source == "merge":
    check_no_conflict(commit_fl)
