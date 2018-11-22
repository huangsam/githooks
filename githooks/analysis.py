import githooks.utils.validation as v
from githooks.constants import (
    MAX_LEN_SUBJECT,
    MAX_LEN_OTHER,
    LABEL_TO_TAG,
    REQUIRED_TAGS,
    OPTIONAL_TAGS,
)


def analyze_file(commit_flname):
    """Analyze contents from commit file.

    Args:
        commit_flname (str): Name of commit file.

    Returns:
        list: Lines inside commit file.
    """
    commit_buffer = []
    with open(commit_flname, 'r') as fl:
        for line in fl.readlines():
            if not line.startswith('#'):
                commit_buffer.append(line)
    assert len(commit_buffer) > 0, 'Empty commit message'
    return commit_buffer


def analyze_tags(subject_line):
    """Analyze subject tags.

    Args:
        subject_line (str): Subject line contents.

    Returns:
        set: Required and optional tags.

    Raises:
        AssertionError: Invalid subject line or bad tags.
    """
    assert v.valid_len(subject_line, MAX_LEN_SUBJECT), 'Subject line too long'
    subject_words = subject_line.split()
    invalid_tags = []
    required_tags = []
    optional_tags = []
    for word in subject_words:
        if word in REQUIRED_TAGS:
            required_tags.append(word)
        elif word in OPTIONAL_TAGS:
            optional_tags.append(word)
        elif word.startswith('[') and word.endswith(']'):
            invalid_tags.append(word)
    assert len(invalid_tags) == 0, 'Invalid tags found'
    assert len(required_tags) == 1, 'Please provide one required tag'
    return set(required_tags + optional_tags) - set(['!!!'])


def analyze_lines(commit_buffer):
    """Analyze non-header lines.

    Args:
        commit_buffer (list): List of non-header lines in commit file.

    Returns:
        list: Last metadata lines.

    Raises:
        AssertionError: Poorly bounded lines in commit buffer.
    """
    last_lines = []
    if len(commit_buffer) > 1:
        for line in commit_buffer:
            assert v.valid_len(line, MAX_LEN_OTHER), 'Other lines are too long'
            if v.valid_kv(line) or v.valid_fixes(line):
                last_lines.append(line)
    return last_lines


def analyze_labels(subject_tags, last_lines):
    """Analyze metadata labels.

    Args:
        subject_tags (list): Subject tags from subject line.
        last_lines (list): Last metadata lines in commit file.

    Raises:
        KeyError: Invalid label(s).
        AssertionError: Invalid label tag(s).
    """
    if '[TASK]' not in subject_tags:
        assert len(last_lines) > 0, 'Required metadata tags'
    labels = map(lambda line: line.split(':')[0], last_lines)
    label_tags = set()
    for label in labels:
        if v.valid_fixes(label):
            return
        tags = LABEL_TO_TAG[label]
        label_tags.update(tags)
    valid_labels = subject_tags.issubset(label_tags)
    valid_labels |= '[TASK]' in subject_tags and len(label_tags) == 0
    assert valid_labels, 'Label tag(s) are invalid'
