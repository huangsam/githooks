# Introduction

These hooks are a collection of policies that I enforced for Python projects at Cisco. Many of them execute the same verification tasks. As such, functionality is centralized into `check_msg.py` and `commons.sh` for reusability.

## Development

These Git hooks utilize a mix of Python and Shell. Python offers a clean approach to procedural programming while Shell offers excellent text processing and file management utilities.

### Python

`check_msg` uses [flake8](https://pypi.python.org/pypi/flake8) to ensure PEP8 compliance, logical flow and complexity bounds. The script ensures that the proposed commit messages are formatted correctly for [JIRA](https://www.atlassian.com/software/jira) pull requests.

### Shell

All the hook shell scripts are written in [Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) and can be easily extended to [Zsh](https://en.wikipedia.org/wiki/Z_shell) if desired. They all use [shellcheck](https://www.shellcheck.net/) to ensure common interpreter pitfalls are prevented from occurring.

## Installation

```bash
curl -fssL huangsam.github.io/githooks/gh-install | bash
```

After installation is complete all scripts and commit message template will be available in your `.git/hooks` directory. If there are any files that already exist with the same name, it will be renamed to `%NAME%.bak`. The git will be configured to point to the commit message template.
