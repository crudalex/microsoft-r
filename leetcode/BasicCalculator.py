    class Solution:
        def calculate(self, s: str):
            length = len(s)
            sign = 1
            result = 0

            stack = list()

            skip = 0
            for i in range(length):
                if skip != 0:
                    skip -= 1
                    continue
                if s[i].isdigit():
                    sum = int(s[i])
                    while i + 1 < length and s[i + 1].isdigit():
                        sum = sum * 10 + int(s[i + 1])
                        i += 1
                        skip += 1

                    result += sum * sign

                elif s[i] == '+':
                    sign = 1
                elif s[i] == '-':
                    sign = -1
                elif s[i] == '(':
                    stack.append(result)
                    stack.append(sign)
                    result = 0
                    sign = 1
                elif s[i] == ')':
                    result = result * stack.pop() + stack.pop()

            return result


    if __name__ == '__main__':
        expr = ["(1+(4+5+2)-3)+(6+8)", " 2-1 + 2 ", "1 + 1"]
        expr = ["2147483647"]
        for i in expr:
            print(Solution().calculate(i))
