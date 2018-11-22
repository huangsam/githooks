from githooks.utils.git import get_repo_from_cwd


def check_non_master():
    repo = get_repo_from_cwd()
    master_checked_out = repo.branches.get('master').is_checked_out()
    assert not master_checked_out, 'Do not commit directly to master'
