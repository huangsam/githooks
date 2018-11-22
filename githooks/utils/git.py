import os

from pygit2 import (
    discover_repository,
    Repository,
)


def get_repo_from_cwd():
    repository_path = discover_repository(os.getcwd())
    return Repository(repository_path)


def get_branch_name(repo):
    head_name = repo.head.shorthand
    return head_name.split('/')[-1]


def get_branch_tag(repo):
    head_name = repo.head.shorthand
    return head_name.split('/')[-2]
