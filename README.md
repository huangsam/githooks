# Introduction

These hooks are the culmination of policies that I typically
enforce for Python projects. Some of these hooks utilize
[flake8](https://pypi.python.org/pypi/flake8) to ensure PEP8
compliance, logical flow and an appropriate level of complexity.
Other hooks utilize the `check-msg` script to ensure that
proposed commit messages are formatted correctly for
[JIRA](https://www.atlassian.com/software/jira) pull requests.

## Implementation

These Git hooks utilize a mix of Python and Shell. Python offers
a clean approach to procedural programming while Shell offers
excellent text processing and file management utilities.

Many of the Git hooks had lines of code that shared common
verification tasks, which resulted in unnecessary bloat. To counter
this effect, verification functionality was centralized into
`check-msg` and `verify` to minimize code redundancy and
maximize hook maintainability.

## Installation

```bash
curl -fssL http://huangsam.github.io/githooks/gh-install | bash
```

After installation is complete all scripts and commit message template
will be available in your `.git/hooks` directory. If there are any
files that already exist with the same name, it will be renamed
to `%NAME%.bak`. The git will be configured to point to the commit
message template.
