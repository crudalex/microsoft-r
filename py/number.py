
def algo(n):
    ret = list()
    start = n * 2 + n
    count = n * 2 + 2
    for i in range(count):
        ret.append(start + i * 2)
    return ret

if __name__ == '__main__':
    for i in range(7):
        print(algo(i))
