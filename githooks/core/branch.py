from githooks.utils.git import is_master_checked_out


def check_non_master():
    assert not is_master_checked_out(), 'Do not commit directly to master'


def check_no_conflict(commit_fl):
    with open(commit_fl, 'r') as f:
        for line in f:
            assert 'Conflicts' not in line
