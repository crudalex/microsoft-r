def seq(n):
    rep = n * 3

    value = n * -n
    print("%d " % (value), end='')
    for i in range(1, rep):
        # value = start + step
        value = value + 2 * i - 1
        print("%d " % (value), end='')
        # step = (i * 2 + 1) + step


# def seq(n):
#     x = -n * n
#     print("%d " % x, end='')
#     for i in range(0, 3 * n):
#         x = x + 2 * i - 1
#         print("%d " % x, end='')

if __name__ == '__main__':
    seq(5)
