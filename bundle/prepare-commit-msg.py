#!/usr/bin/env python
import sys

# Tag name
tag = sys.argv[1]

# Can be (message, merge, template)
action = sys.argv[2]

print(tag, action)
