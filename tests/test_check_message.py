import os

from githooks.core.message import check_message
from tests import fixt_path


def test_check_message():
    commit_fl = os.path.join(fixt_path, 'sample-commit.txt')
    check_message(commit_fl)
