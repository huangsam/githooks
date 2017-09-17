# Installation

```bash
curl -fssL huangsam.github.io/githooks/gh-install | bash
```

After installation is complete all scripts and commit message template will be available in your `.git/hooks` directory. If there are any files that already exist with the same name, it will be renamed to `%NAME%.bak`. The git will be configured to point to the commit message template.
