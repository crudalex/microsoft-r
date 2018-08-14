class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        from itertools import combinations
        c = combinations(nums, 2)

        # for (i, n) in enumerate(nums):
        #     for (j, m) in enumerate(nums):
        #         if i == j:
        #             continue
        #         if n + m == target:
        #             return (i, j)

        # sums = dict()
        # for s in frozenset(c):
        #     sums[s] = sum(s)
        #
        # for k in sums.keys():
        #     if sums[k] == target:
        #         (i, j) == list(k)
        #         return (nums.index(i), nums.index(j))
        #
        # return None

        h = dict()
        for (i, j) in enumerate(nums):
            c = target - j
            if c in h:
                return (i, h[c])

            h[j] = i


if __name__ == '__main__':
    # nums = [2, 7, 11, 15]
    # target = 9

    nums = [3, 2, 4]
    target = 6

    s = Solution()
    print(s.twoSum(nums, target))
