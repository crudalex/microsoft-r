import re
import sys

vowels = 'aeiou'
consonants = 'qwrtypsdfghjklzxcvbnm'

string = sys.stdin.readline()
string = re.sub('^[%s]+' % vowels, '', string, re.IGNORECASE)
string = re.sub('[%s]+$' % vowels, '', string, re.IGNORECASE)

substrings = re.split('[%s]+' % consonants, string, re.IGNORECASE | re.MULTILINE)

matches = []
for s in substrings:
    if re.search('^[%s]{2,}$' % vowels, s, re.IGNORECASE):
        matches.append(s)

if len(matches) == 0:
    print("-1")
    exit(0)

for m in matches:
    print(m)


