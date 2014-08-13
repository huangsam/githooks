#!/usr/bin/env python

from __future__ import print_function
import sys

MAX_SLEN = 52
MAX_OLEN = 72


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


def verify_subject_tags(subject_line):
    invalid_tags, required_tags, _ = analyze_tags(subject_line)
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
    other_violation = reduce(lambda x, y: x | y,
                             map(line_exceeds, other_lines))

    if other_violation is True:
        warning('Other lines too long (MAX %i chars)' % MAX_OLEN)
        exit(5)


def verify_metadata(last_line):
    try:
        metadata_label, _ = last_line.split(':')

        if metadata_label not in ('Closes-Bug',
                                  'Partial-Bug',
                                  'Related-Bug',
                                  'Implements',
                                  'UpgradeImpact',
                                  'SecurityImpact',
                                  'DocImpact'):
            warning('Invalid metadata label: %s' % metadata_label)
            exit(6)
    except ValueError:
        warning('Corresponding metadata label is missing')
        exit(7)


def main():
    commit_flname = sys.argv[1]
    commit_fl = open(commit_flname)

    try:
        subject_line = commit_fl.readline()
        other_lines = commit_fl.readlines()
        last_line = other_lines[-1]
    except IndexError:
        warning('One-liners are unacceptable')
        exit(8)

    verify_subject_length(subject_line)
    verify_subject_tags(subject_line)
    verify_other_lengths(other_lines)
    verify_metadata(last_line)

if __name__ == '__main__':
    main()
