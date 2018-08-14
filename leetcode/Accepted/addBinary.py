class Solution:
    def addBinary(self, a, b):
        sum = int(a, 2) + int(b, 2)
        return bin(sum)[2:]


if __name__ == '__main__':
    s1 = Solution().addBinary('11', '1')
    print(s1)

    s2 = Solution().addBinary('1010', '1011')
    print(s2)
