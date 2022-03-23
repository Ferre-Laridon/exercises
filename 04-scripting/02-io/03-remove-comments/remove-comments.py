from fileinput import filename
import sys
import re

def remove_comments(filename):
    with open(filename, 'r') as remove:
        lines = remove.read()

    lines = re.sub('#.*$', '', lines, flags=re.MULTILINE)

    with open(filename, 'w') as removed:
        removed.write(lines)
        

for file in sys.argv[1:]:
    remove_comments(file)