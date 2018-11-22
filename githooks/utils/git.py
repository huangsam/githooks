import os

from pygit2 import (
    discover_repository,
    Repository,
)


def _get_repo_from_cwd():
    repository_path = discover_repository(os.getcwd())
    return Repository(repository_path)


def get_branch_tag():
    repo = _get_repo_from_cwd()
    head_name = repo.head.shorthand
    return head_name.split('/')[0]


def get_branch_name():
    repo = _get_repo_from_cwd()
    head_name = repo.head.shorthand
    return head_name.split('/')[1]
