import githooks.utils.validation as v
from githooks.constants import LABEL_TO_TAG, MAX_LEN_OTHER, MAX_LEN_SUBJECT, OPTIONAL_TAGS, REQUIRED_TAGS, CommitTag


class CommitMessageScanner:
    """Commit message scanner.

    Scans for anomalies in the commit message and reports them back
    to the caller via exceptions such as AssertionError and KeyError.
    """

    def __init__(self, commit_flname: str) -> None:
        self.commit_flname = commit_flname
        self.commit_lines: list[str] = []
        self.subject_tags: set[str] = set()
        self.subject_line: str = ""
        self.non_headers: list[str] = []

    def scan(self) -> None:
        self.scan_commit_lines()
        self.scan_subject_line()
        self.scan_subject_tags()
        self.scan_non_headers()
        self.scan_labels()

    def scan_commit_lines(self) -> None:
        with open(self.commit_flname, "r") as fl:
            for line in fl.readlines():
                if not line.startswith("#"):
                    self.commit_lines.append(line)
        assert len(self.commit_lines) > 0, "Empty commit message"

    def scan_subject_line(self) -> None:
        self.subject_line = self.commit_lines.pop(0)
        assert v.valid_len(self.subject_line, MAX_LEN_SUBJECT), "Subject line too long"

    def scan_subject_tags(self) -> None:
        invalid_tags = []
        required_tags = []
        optional_tags = []
        for word in self.subject_line.split():
            if word in REQUIRED_TAGS:
                required_tags.append(word)
            elif word in OPTIONAL_TAGS:
                optional_tags.append(word)
            elif word.startswith("[") and word.endswith("]"):
                invalid_tags.append(word)
        assert len(invalid_tags) == 0, "Invalid tags found"
        assert len(required_tags) == 1, "Please provide one required tag"
        self.subject_tags = set(required_tags + optional_tags) - set([CommitTag.MARKER])

    def scan_non_headers(self) -> None:
        for line in self.commit_lines:
            assert v.valid_len(line, MAX_LEN_OTHER), "Other lines are too long"
            if v.valid_kv(line) or v.valid_fixes(line):
                self.non_headers.append(line)

    def scan_labels(self) -> None:
        if "[TASK]" not in self.subject_tags:
            assert len(self.non_headers) > 0, "Required metadata tags"
        labels = map(lambda line: line.split(":")[0], self.non_headers)
        label_tags = set()
        for label in labels:
            if v.valid_fixes(label):
                return
            tags = LABEL_TO_TAG[label]
            label_tags.update(tags)
        valid_labels = self.subject_tags.issubset(label_tags)
        valid_labels |= CommitTag.TASK in self.subject_tags and len(label_tags) == 0
        assert valid_labels, "Label tag(s) are invalid"
