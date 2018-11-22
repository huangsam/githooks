def check_no_conflict(commit_fl):
    with open(commit_fl, 'r') as f:
        for line in f:
            assert 'Conflicts' not in line
