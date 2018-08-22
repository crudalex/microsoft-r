class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        digits = [int(i) for i in list(str(N))]

        for i in range(0, len(digits) - 1):

            if digits[i + 1] == 0:
                digits[i] = digits[i]


if __name__ == '__main__':
    s1 = Solution().monotoneIncreasingDigits(10)
    s2 = Solution().monotoneIncreasingDigits(1234)
    s3 = Solution().monotoneIncreasingDigits(332)
