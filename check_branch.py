#!/usr/bin/env python
import os

from pygit2 import (
    discover_repository,
    Repository,
)


def main():
    current_working_directory = os.getcwd()
    repository_path = discover_repository(current_working_directory)
    repo = Repository(repository_path)
    master_checked_out = repo.branches.get('master').is_checked_out()
    assert not master_checked_out, 'Do not commit directly to master'


if __name__ == '__main__':
    main()
