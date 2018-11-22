import os

from pygit2 import (
    discover_repository,
    Repository,
)


def get_repo_from_cwd():
    current_working_directory = os.getcwd()
    repository_path = discover_repository(current_working_directory)
    return Repository(repository_path)


def get_branch_name(repo):
    return repo.head.name.split('/')[-1]
