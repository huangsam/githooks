#!/usr/bin/env python

from __future__ import print_function
import io
import sys

MAX_SLEN = 52
MAX_OLEN = 72

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


def good_labels(subject_tags, labels):
    label_tags = set()

    for label in labels:
        tags = LABEL_TO_TAG.get(label)

        if tags is None:
            return False

        label_tags.update(tags)

    if subject_tags.issubset(label_tags):
        return True
    elif '[TASK]' in subject_tags and len(label_tags) == 0:
        return True
    else:
        return False


def analyze_tags(line):
    invalid_tags = []
    required_tags = []
    supplemental_tags = []

    subject_words = line.split()

    for word in subject_words:
        if word in ('[BUGFIX]',
                    '[TASK]',
                    '[FEATURE]'):
            required_tags.append(word)
        elif word in ('[!!!]',
                      '[API]',
                      '[CONF]',
                      '[DB]',
                      '[SECURITY]'):
            supplemental_tags.append(word)
        elif word.startswith('[') and word.endswith(']'):
            invalid_tags.append(word)

    return (invalid_tags, required_tags, supplemental_tags)


def line_exceeds(line, max_len=MAX_OLEN):
    return True if len(line) > max_len else False


def warning(str):
    print('[POLICY]', str, file=sys.stderr)


def verify_subject_length(subject_line):
    if line_exceeds(subject_line, MAX_SLEN):
        warning('Subject line too long (MAX %i chars)' % MAX_SLEN)
        exit(1)


def verify_subject_tags(invalid_tags, required_tags):
    num_invalid = len(invalid_tags)
    num_require = len(required_tags)

    if num_invalid > 0:
        invalid_str = ', '.join(invalid_tags)
        warning('Invalid tag(s): %s' % invalid_str)
        exit(2)

    if num_require == 0:
        warning('Required commit tag is missing')
        exit(3)
    elif num_require > 1:
        warning('Provide just one required tag')
        exit(4)


def verify_other_lengths(other_lines):
    # aggregate line_exceed results
    other_violation = reduce(lambda x, y: x | y,
                             map(line_exceeds, other_lines))

    if other_violation is True:
        warning('Other lines too long (MAX %i chars)' % MAX_OLEN)
        exit(5)


def verify_metadata(valid_tags, last_lines):
    subject_tags = set(valid_tags)
    subject_tags.discard('[!!!]')

    if '[TASK]' not in subject_tags and len(last_lines) == 0:
        warning('Required metadata tags')
        exit(6)

    # collect metadata labels
    labels = map(lambda l: l.split(':')[0], last_lines)

    if good_labels(subject_tags, labels) is False:
        warning('Invalid metadata label(s)')
        exit(7)


def main():

    commit_flname = sys.argv[1]

    with io.open(commit_flname) as fl:
        commit_fl = fl.read().splitlines()

    # ignore comments
    commit_fl = filter(
        lambda l: not l.startswith('#'), commit_fl)

    if len(commit_fl) == 0:
        warning('Empty commit message')
        exit(8)

    subject_line = commit_fl.pop(0)
    i_tags, r_tags, s_tags = analyze_tags(subject_line)
    valid_tags = r_tags + s_tags

    verify_subject_length(subject_line)
    verify_subject_tags(i_tags, r_tags)

    if len(commit_fl) > 1:
        verify_other_lengths(commit_fl)

    # select metadata lines
    last_lines = filter(
        lambda l: len(l.split(':')) == 2, commit_fl)

    verify_metadata(valid_tags, last_lines)

if __name__ == '__main__':
    main()
