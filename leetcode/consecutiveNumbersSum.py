class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """

        def can_sum(start, N):

            sum = 0

            for i in range(start, N):
                sum += i

                if sum == N:
                    return True

                if sum > N:
                    return False

        cans = 1
        for i in range(1, round(N / 2 + 1)):
            if can_sum(i, N):
                cans += 1

        return cans


if __name__ == '__main__':
    # n = [3, 9, 20, None, None, 15, 7]

    for i in [5, 9, 15]:
        s = Solution().consecutiveNumbersSum(i)

        from pprint import pprint

        pprint(s)

if __name__ == '__main__':
    # n = [3, 9, 20, None, None, 15, 7]

    for i in [100000]:
        s = Solution().consecutiveNumbersSum(i)

        from pprint import pprint

        pprint(s)
