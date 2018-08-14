class Solution:
    def plusOne(self, digits):
        r = [str(i) for i in digits]
        r = ''.join(r)
        r = int(r) + 1
        r = list(str(r))
        r = [int(i) for i in r]
        return r

if __name__ == '__main__':
    s1 = Solution().plusOne([1, 2, 3])
    print(s1)

    # s2 = Solution().plusOne([4, 3, 2, 1])
    # print(s2)
