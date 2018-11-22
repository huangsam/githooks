#!/usr/bin/env python
import os

from githooks.core.syntax import check_flake8

repo_path = os.path.dirname(os.path.realpath(__name__))
check_flake8(repo_path)
