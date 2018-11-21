#!/usr/bin/env python
import argparse
import sys

import githooks.analysis as a


def parse_args(argv):
    parser = argparse.ArgumentParser(
        description='Check correctness of commit message.',
        add_help=True)
    parser.add_argument(
        'filename',
        type=str,
        help='File path of commit message')
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    commit_buffer = a.analyze_file(args.filename)
    subject_tags = a.analyze_tags(commit_buffer.pop(0))
    last_lines = a.analyze_lines(commit_buffer)
    a.analyze_labels(subject_tags, last_lines)


if __name__ == '__main__':
    main(sys.argv[1:])
