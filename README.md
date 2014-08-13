# Introduction

These hooks are the culmination of policies that I typically
enforce for Python projects. Some of these hooks utilize
[flake8](https://pypi.python.org/pypi/flake8) to ensure PEP8
compliance, logical flow and an appropriate level of complexity.
Other hooks utilize the `check-msg` script to ensure that
proposed commit messages are formatted correctly for
[JIRA](https://www.atlassian.com/software/jira) pull requests.

## Design Decisions

These Git hooks utilize a mix of Python and Shell. Python offers
a clean approach to procedural programming while Shell offers
excellent text processing and file management utilities.

Many of the Git hooks had lines of code that shared common
verification tasks, which resulted in unnecessary bloat. To counter
this effect, verification functionality was centralized into
`check-msg` and `verify` to minimize code redundancy and
maximize hook maintainability.

## Installation

Run the `generate-hooks.sh` script to generate the necessary
hook executables. All executables should now reside in the newly
created `hooks` folder. Finally, replace the `.git/hooks` folder
within your desired project with the generated `hooks` folder
to enable project policies.
