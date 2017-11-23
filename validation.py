def valid_len(line, max_len):
    """Check if line length is valid.

    Args:
        line (str): Collection of words.
        max_len (int): Maximum length enforced.

    Returns:
        bool: Flag for valid line length.
    """
    return len(line) <= max_len


def valid_kv(line):
    """Check if line is valid key:value.

    Args:
        line (str): Textual content.

    Returns:
        bool: Flag for valid key:value.
    """
    return len(line.split(':')) == 2


def valid_fixes(line):
    """Check if line is valid 'fixes' statement.

    Args:
        line (str): Textual content.

    Returns:
        bool: Flag for valid 'fixes' statement.
    """
    return line.lower().startswith('fixes #')
