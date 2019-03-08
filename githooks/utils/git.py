import os

from git import Repo


def _get_repo_from_cwd():
    return Repo(os.getcwd(), search_parent_directories=True)


def _get_branch_name():
    repo = _get_repo_from_cwd()
    return repo.active_branch.name


def get_branch_tag():
    return _get_branch_name().split("/")[0]


def get_branch_title():
    return _get_branch_name().split("/")[1]


def is_master_checked_out():
    return _get_branch_name() == "master"
