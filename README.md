# Introduction

These hooks are a collection of policies that I enforced for Python projects at Cisco. `check_msg` uses [flake8](https://pypi.python.org/pypi/flake8) to ensure PEP8 compliance, logical flow and complexity bounds. Some hooks use the script to ensure that the proposed commit messages are formatted correctly for [JIRA](https://www.atlassian.com/software/jira) pull requests.

## Implementation

These Git hooks utilize a mix of Python and Shell. Python offers a clean approach to procedural programming while Shell offers excellent text processing and file management utilities.

Many of the Git hooks execute the same verification tasks. As such, common functionality is centralized into `check_msg` and `commons` for maximum code reusability and hook maintainability.

## Installation

```bash
curl -fssL huangsam.github.io/githooks/gh-install | bash
```

After installation is complete all scripts and commit message template will be available in your `.git/hooks` directory. If there are any files that already exist with the same name, it will be renamed to `%NAME%.bak`. The git will be configured to point to the commit message template.
