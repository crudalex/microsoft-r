class Solution:
    def rob(self, nums):
        evens = nums[0::2]
        odds = nums[1::2]

        return max(sum(evens), sum(odds))


if __name__ == '__main__':
    s1 = Solution().rob([1, 2, 3, 1])
    print(s1)
    s2 = Solution().rob([2, 7, 9, 3, 1])
    print(s2)
