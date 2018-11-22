from githooks.utils.git import get_repo_from_cwd


def check_non_master():
    repo = get_repo_from_cwd()
    master_checked_out = repo.branches.get('master').is_checked_out()
    assert not master_checked_out, 'Do not commit directly to master'


def check_no_conflict(commit_fl):
    with open(commit_fl, 'r') as f:
        for line in f:
            assert 'Conflicts' not in line
