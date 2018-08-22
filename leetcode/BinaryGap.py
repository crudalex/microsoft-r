class Solution:
    def binaryGap(self, N):
        bitmap = list(bin(N)[2:])
        ones = []
        for i, j in enumerate(bitmap):
            if j == "1":
                ones.append(i)

        def walk(l):
            if len(l) == 0 or len(l) == 1:
                return 0

            return max(l[0] - l[1], walk(l[1:]))

        return walk(ones)


if __name__ == '__main__':
    s1 = Solution().binaryGap(22)
    s2 = Solution().binaryGap(5)
    s3 = Solution().binaryGap(6)
    s4 = Solution().binaryGap(8)
