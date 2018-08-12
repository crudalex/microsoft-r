class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        def rotate(i):
            k = ['0', '1', '2', '5', '6', '8', '9']
            v = ['0', '1', '5', '2', '9', '8', '6']
            r = dict(zip(k, v))

            s = [r[c] for c in str(i)]
            s = ''.join(s)

            return int(s)

        count = 0
        import re
        for i in range(1, N+1):
            if re.search('[347]+', str(i)):
                continue

            if i == rotate(i):
                continue

            count += 1

        return count


if __name__ == '__main__':
    from pprint import pprint

    N = 2
    s = Solution().rotatedDigits(N)
    pprint(s)
