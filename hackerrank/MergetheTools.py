def merge_the_tools(string, k):
  length = len(string)
  line_size = int(length / k)

  if line_size == length:
    line_size = 1

  for i in range(0, length, line_size):
    char_set = set()
    for j in range(i, i + line_size):
      char = string[j]
      if string[j] not in char_set:
        print("%s" % char, end="")
        char_set.add(char)
    print("")


if __name__ == '__main__':
  string, k = input(), int(input())
  merge_the_tools(string, k)
