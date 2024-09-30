from githooks.constants import TRUNK_BRANCHES
from githooks.utils.git import branch_name


def check_no_trunk() -> None:
    assert branch_name() not in TRUNK_BRANCHES, "Do not commit changes to trunk"


def check_no_conflict(commit_fl: str) -> None:
    with open(commit_fl, "r") as f:
        for line in f:
            assert "Conflicts" not in line, "Please resolve merge conflicts"
