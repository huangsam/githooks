def valid_len(line, max_len):
    return len(line) <= max_len


def valid_kv(line):
    return len(line.split(':')) == 2


def valid_fixes(line):
    return line.lower().startswith('fixes #')
