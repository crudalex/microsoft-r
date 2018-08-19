class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        try:
            index = haystack.index(needle)
        except ValueError:
            index = -1

        return index

if __name__ == '__main__':

    s1 = Solution().strStr("hello", "ll")

    s2 = Solution().strStr("aaaaa", "bba")

