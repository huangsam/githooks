from githooks.scanner import CommitMessageScanner


def check_message(commit_fl: str) -> None:
    CommitMessageScanner(commit_fl).scan()
