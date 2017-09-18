#!/usr/bin/env python

import argparse
import sys


# Max length of subject line
MAX_LEN_SUBJECT = 52

# Max length of other lines
MAX_LEN_OTHER = 72

# Label to tag mapping
LABEL_TO_TAG = {
    'Closes-Bug': set(['[BUGFIX]']),
    'DocImpact': set(['[SECURITY]', '[TASK]']),
    'Implements': set(['[FEATURE]', '[TASK]']),
    'Partial-Bug': set(['[BUGFIX]']),
    'Related-Bug': set(['[BUGFIX]', '[FEATURE]']),
    'SecurityImpact': set(['[SECURITY]']),
    'UpgradeImpact': set(),
}

# Tags that apply to all labels
for label in LABEL_TO_TAG.keys():
    LABEL_TO_TAG[label].add('[API]')
    LABEL_TO_TAG[label].add('[CONF]')
    LABEL_TO_TAG[label].add('[DB]')

# Special tags
REQUIRED_TAGS = set(['[BUGFIX]', '[TASK]', '[FEATURE]'])
OPTIONAL_TAGS = set(['[!!!]', '[API]', '[CONF]', '[DB]', '[SECURITY]'])


def parse_args(argv):
    """Parse command-line arguments.

    Args:
        argv (list): Command line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description='Check correctness of commit message.',
        add_help=True)
    parser.add_argument(
        'filename',
        type=str,
        help='Filename of commit message')
    return parser.parse_args(argv)


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
    assert valid_len(subject_line, MAX_LEN_SUBJECT), 'Subject line too long'
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
            assert valid_len(line, MAX_LEN_OTHER), 'Other lines are too long'
            if valid_kv(line) or valid_fixes(line):
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
        if valid_fixes(label):
            return
        tags = LABEL_TO_TAG[label]
        label_tags.update(tags)
    valid_labels = subject_tags.issubset(label_tags)
    valid_labels |= '[TASK]' in subject_tags and len(label_tags) == 0
    assert valid_labels, 'Label tag(s) are invalid'


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


def main():
    args = parse_args(sys.argv[1:])
    commit_buffer = analyze_file(args.filename)
    subject_tags = analyze_tags(commit_buffer.pop(0))
    last_lines = analyze_lines(commit_buffer)
    analyze_labels(subject_tags, last_lines)


if __name__ == '__main__':
    main()
