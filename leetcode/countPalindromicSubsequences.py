class Solution:
    def countPalindromicSubsequences(self, S):
        pass

if __name__ == '__main__':
    s1 = Solution().countPalindromicSubsequences('bccb')
    print(s1 == 6)

    s2 = Solution().countPalindromicSubsequences('abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba')
    print(s2 == 104860361)