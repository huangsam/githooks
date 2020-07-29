# githooks

[![CircleCI](https://circleci.com/gh/huangsam/githooks.svg?style=svg)](https://circleci.com/gh/huangsam/githooks)

These hooks started out as a collection of policies that I enforced for Python
projects at [Cisco](https://www.cisco.com/). Many of them execute the
same verification tasks. As such, functionality is centralized into `githooks`
package for reusability.

## Development

These Git hooks utilize all Python for consistency.

## Installation

```bash
curl -fssL huangsam.github.io/githooks/gh-install | bash
```

After installation is complete all scripts and commit message template will
be available in your `.git/hooks` directory.
