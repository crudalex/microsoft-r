class Solution:
    def addStrings(self, num1:str, num2:str):

        num1, num2 = list(num1), list(num2)
        carry, res = 0, []

        while len(num2) > 0 or len(num1) > 0:

            # get int
            n1 = ord(num1.pop()) - ord('0') if len(num1) > 0 else 0
            n2 = ord(num2.pop()) - ord('0') if len(num2) > 0 else 0

            # get sum from two numbers plus carry from last iteration
            temp = n1 + n2 + carry

            # add mod to response
            res.append(temp % 10)

            # get carry
            carry = temp // 10

        # add carry to last iteration
        if carry: res.append(carry)

        # convert int array to string arrays, join and reverse using negative step
        return ''.join([str(i) for i in res])[::-1]


if __name__ == '__main__':
    s1 = Solution().addStrings('2', '3')
    s2 = Solution().addStrings('123', '456')

    print(s1)
    print(s2)
