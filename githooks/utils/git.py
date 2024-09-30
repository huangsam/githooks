import os

from git import Repo


def _repo() -> Repo:
    return Repo(os.getcwd(), search_parent_directories=True)


def branch_name() -> str:
    return _repo().active_branch.name


def branch_tag() -> str:
    return branch_name().split("/")[0]
