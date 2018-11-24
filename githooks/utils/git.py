import os

from git import Repo


def _get_repo_from_cwd():
    return Repo(os.getcwd(), search_parent_directories=True)


def get_branch_tag():
    repo = _get_repo_from_cwd()
    head_name = repo.active_branch.name
    return head_name.split('/')[0]


def get_branch_name():
    repo = _get_repo_from_cwd()
    head_name = repo.active_branch.name
    return head_name.split('/')[1]


def is_master_checked_out():
    repo = _get_repo_from_cwd()
    return repo.active_branch.name == 'master'
