import timeit


# class Solution(object):
#     def rob(self, nums):

#         if (len(nums) == 0):
#             return 0
#         elif (len(nums) == 1):
#             return nums[0]
#         else:
#             dp = [0] * (len(nums) + 2)
#             for i in range(2, len(nums) + 2):
#                 dp[i] = max(dp[i - 2] + nums[i - 2], dp[i - 1])
#         return dp[len(nums) + 1]


class Solution:

    def __init__(self):

        self.cache = dict()

    def rob(self, nums):

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            c1 = nums[0] + self.rob(nums[2:])
            c2 = self.rob(nums[1:])
            self.cache[len(nums)] = max(c1, c2)
            return self.cache[len(nums)]


if __name__ == '__main__':

    lists = [[183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235,
              50, 81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]]

    # lists = [[1, 2, 3, 1], [2, 7, 9, 3, 1], [1, 2]]

    for i in lists:
        t1 = timeit.default_timer()
        s = Solution().rob(i)
        t2 = timeit.default_timer()
        delta = t2 - t1
        print("max: %s, took %.6f" % (s, delta))
