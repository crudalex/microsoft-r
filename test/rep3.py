def rep3(n: int):
    rep = n * 2

    for i in range(0, rep):
        if i < n:
            d = i * 2
        else:
            d = i
        print("%d " % d, end='')


if __name__ == '__main__':
    with open('hello.txt', 'w+') as f:
        f.seek(1024 * 1024)
        f.write('\0')
