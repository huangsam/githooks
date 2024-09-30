from githooks.scanner import CommitScanner


def check_message(commit_fl: str) -> None:
    CommitScanner(commit_fl).scan()
