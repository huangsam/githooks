#!/usr/bin/env python

import sys


# Max length of subject line
MAX_SLEN = 52

# Max length of other lines
MAX_OLEN = 72

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

for key in LABEL_TO_TAG.keys():
    LABEL_TO_TAG[key].add('[API]')
    LABEL_TO_TAG[key].add('[CONF]')
    LABEL_TO_TAG[key].add('[DB]')

REQUIRED_TAGS = set(['[BUGFIX]', '[TASK]', '[FEATURE]'])
OPTIONAL_TAGS = set(['[!!!]', '[API]', '[CONF]', '[DB]', '[SECURITY]'])


def analyze_tags(line):
    """Analyze tags.

    Args:
        line (str): Collection of words.

    Returns:
        tuple: Required and optional tags.
    """
    invalid_tags = []
    required_tags = []
    optional_tags = []
    subject_words = line.split()
    for word in subject_words:
        if word in REQUIRED_TAGS:
            required_tags.append(word)
        elif word in OPTIONAL_TAGS:
            optional_tags.append(word)
        elif word.startswith('[') and word.endswith(']'):
            invalid_tags.append(word)
    assert len(invalid_tags) == 0, 'Invalid tags found'
    assert len(required_tags) == 1, 'Please provide one required tag'
    return (required_tags, optional_tags)


def line_exceeds(line, max_len=MAX_OLEN):
    """Check if line exceeds specified length.

    Args:
        line (str): Collection of words.
        max_len (int): Maximum length enforced.

    Returns:
        bool: Flag for exceeding max length
    """
    return True if len(line) > max_len else False


def valid_metadata(val):
    """Check if metadata is valid.

    Args:
        val (str): Textual content.

    Returns:
        bool: Flag for valid metadata.
    """
    return len(val.split(':')) == 2 or val.lower().startswith('fixes #')


def verify_labels(subject_tags, labels):
    """Checks if labels are good.

    Args:
        subject_tags (list): Subject tags.
        labels (list): Labels.

    Raises:
        AssertionError: From improper labels.
    """
    label_tags = set()
    for label in labels:
        if label.lower().startswith('fixes #'):
            return
        tags = LABEL_TO_TAG.get(label)
        assert tags, 'Invalid metadata label'
        label_tags.update(tags)
    valid_labels = subject_tags.issubset(label_tags)
    valid_labels |= '[TASK]' in subject_tags and len(label_tags) == 0
    assert valid_labels, 'Label tag(s) are invalid'


def main():
    commit_flname = sys.argv[1]
    commit_buffer = []

    with open(commit_flname) as fl:
        for line in fl.readlines():
            if not line.startswith('#'):
                commit_buffer.append(line)
    assert len(commit_buffer) > 0, 'Empty commit message'

    subject_line = commit_buffer.pop(0)
    assert not line_exceeds(subject_line, MAX_SLEN), 'Subject line too long'

    required_tags, optional_tags = analyze_tags(subject_line)
    valid_tags = required_tags + optional_tags
    subject_tags = set(valid_tags)
    subject_tags.discard('[!!!]')
    last_lines = []
    if len(commit_buffer) > 1:
        for line in commit_buffer:
            assert line_exceeds(line) is False, 'Other lines are too long'
            if valid_metadata(line):
                last_lines.append(line)
    if '[TASK]' not in subject_tags:
        assert len(last_lines) > 0, 'Required metadata tags'
    labels = map(lambda line: line.split(':')[0], last_lines)
    verify_labels(subject_tags, labels)


if __name__ == '__main__':
    main()
