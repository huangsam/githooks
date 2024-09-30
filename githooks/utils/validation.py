def valid_len(line: str, max_len: int) -> bool:
    return len(line) <= max_len


def valid_kv(line: str) -> bool:
    return len(line.split(":")) == 2


def valid_fixes(line) -> bool:
    return line.lower().startswith("fixes #")
