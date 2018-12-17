def minion_game(string):
  vowels = ['A', 'E', 'I', 'O', 'U']

  kevin = 0
  length = len(string)
  for (i, j) in enumerate(string):
    if j in vowels:
      kevin += length - i

  stuart = length * (length + 1) / 2 - kevin

  if stuart > kevin:
    print("Stuart %d" % stuart)
    return

  if kevin > stuart:
    print("Kevin %d" % kevin)
    return

  if kevin == stuart:
    print("Draw")
    return


if __name__ == '__main__':
  s = input()
  minion_game(s)
