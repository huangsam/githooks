# githooks

![](https://img.shields.io/circleci/build/github/huangsam/githooks)
![](https://img.shields.io/github/license/huangsam/githooks)

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
