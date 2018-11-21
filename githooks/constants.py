# Max length of subject line
MAX_LEN_SUBJECT = 52

# Max length of other lines
MAX_LEN_OTHER = 72

# Label to tag mapping
LABEL_TO_TAG = {
    'Closes-Bug': set(['[BUGFIX]']),
    'DocImpact': set(['[SECURITY]', '[TASK]']),
    'Implements': set(['[FEATURE]', '[TASK]']),
    'Partial-Bug': set(['[BUGFIX]']),
    'Related-Bug': set(['[BUGFIX]', '[FEATURE]']),
    'SecurityImpact': set(['[SECURITY]']),
    'UpgradeImpact': set(),
}

# Tags that apply to all labels
for label in LABEL_TO_TAG.keys():
    LABEL_TO_TAG[label].add('[API]')
    LABEL_TO_TAG[label].add('[CONF]')
    LABEL_TO_TAG[label].add('[DB]')

# Special tags
REQUIRED_TAGS = set(['[BUGFIX]', '[TASK]', '[FEATURE]'])
OPTIONAL_TAGS = set(['[!!!]', '[API]', '[CONF]', '[DB]', '[SECURITY]'])
