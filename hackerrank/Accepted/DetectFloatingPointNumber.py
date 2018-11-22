import re
import sys


def is_float(s):
    """

    :type s: str
    """
    if not re.search('^[0-9+-\.]+$', s):
        return False

    if re.search('\-{1}', s):
        if re.search('\+{1}', s):
            return False

    if not re.search('\.{1}', s):
        return False
    
    try: 
        n = float(s)
    except ValueError:
        return False

    return True


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for _ in range(n):
        s = sys.stdin.readline()
        print("%s" % is_float(s))
