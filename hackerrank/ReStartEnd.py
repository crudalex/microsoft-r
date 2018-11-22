import sys
import re

# Enter your code here. Read input from STDIN. Print output to STDOUT

s = sys.stdin.readline()
k = sys.stdin.readline()

matches = re.finditer('%s' % k, s, re.MULTILINE)

c = 0
for m in matches:
    print("(%d, %d)" % (m.start(), m.end()))
    c += 1

if c == 0:
    print("(-1, -1)")
