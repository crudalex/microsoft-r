import re

line = input()

match = re.search("([\-\+]*\d+)([\-\+]*\d+)j", line)

x = int(match.group(1))
y = int(match.group(2))

from cmath import phase

z = complex(x, y)
print(abs(z))
print(phase(z))
