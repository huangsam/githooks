# Max length of subject line
MAX_LEN_SUBJECT = 52

# Max length of other lines
MAX_LEN_OTHER = 72


class CommitLabel:
    BUG_CLOSE = "Closes-Bug"
    BUG_PARTIAL = "Partial-Bug"
    BUG_RELATED = "Related-Bug"
    IMPACT_DOC = "DocImpact"
    IMPACT_SECURITY = "SecurityImpact"
    IMPACT_UPGRADE = "UpgradeImpact"
    IMPLEMENTS = "Implements"


class CommitTag:
    API = "[API]"
    BUGFIX = "[BUGFIX]"
    CONFIG = "[CONF]"
    DATABASE = "[DB]"
    FEATURE = "[FEATURE]"
    MARKER = "[!!!]"
    SECURITY = "[SECURITY]"
    TASK = "[TASK]"


class TrunkBranch:
    MASTER = "master"
    MAIN = "main"


# Label to tag mapping
LABEL_TO_TAG = {
    CommitLabel.BUG_CLOSE: {CommitTag.BUGFIX},
    CommitLabel.BUG_PARTIAL: {CommitTag.BUGFIX},
    CommitLabel.BUG_RELATED: {CommitTag.BUGFIX, CommitTag.FEATURE},
    CommitLabel.IMPACT_DOC: {CommitTag.SECURITY, CommitTag.TASK},
    CommitLabel.IMPACT_SECURITY: {CommitTag.SECURITY},
    CommitLabel.IMPACT_UPGRADE: set(),
    CommitLabel.IMPLEMENTS: {CommitTag.FEATURE, CommitTag.TASK},
}

# Tags that apply to all labels
for label in LABEL_TO_TAG.keys():
    LABEL_TO_TAG[label].add(CommitTag.API)
    LABEL_TO_TAG[label].add(CommitTag.CONFIG)
    LABEL_TO_TAG[label].add(CommitTag.DATABASE)

# Special tags
REQUIRED_TAGS = set([CommitTag.BUGFIX, CommitTag.TASK, CommitTag.FEATURE])
OPTIONAL_TAGS = set([CommitTag.MARKER, CommitTag.API, CommitTag.CONFIG, CommitTag.DATABASE, CommitTag.SECURITY])

# Trunk branches
TRUNK_BRANCHES = {TrunkBranch.MASTER, TrunkBranch.MAIN}
