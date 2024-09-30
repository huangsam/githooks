from githooks.core.message import check_message
from tests import FIXTURE_PATH


def test_check_message():
    check_message(FIXTURE_PATH / "sample-commit.txt")
