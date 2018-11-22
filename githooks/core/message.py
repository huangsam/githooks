import githooks.analysis as a


def check_message(filename):
    commit_buffer = a.analyze_file(filename)
    subject_tags = a.analyze_tags(commit_buffer.pop(0))
    last_lines = a.analyze_lines(commit_buffer)
    a.analyze_labels(subject_tags, last_lines)
