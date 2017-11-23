#!/usr/bin/env python
import argparse
import sys

import analysis as a


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


def main():
    args = parse_args(sys.argv[1:])
    commit_buffer = a.analyze_file(args.filename)
    subject_tags = a.analyze_tags(commit_buffer.pop(0))
    last_lines = a.analyze_lines(commit_buffer)
    a.analyze_labels(subject_tags, last_lines)


if __name__ == '__main__':
    main()
