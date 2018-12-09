class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        


if __name__ == '__main__':
    s = Solution()
    assert 2 == s.findMedianSortedArrays([1, 3], [2])
    assert 2.5 == s.findMedianSortedArrays([1, 2], [3, 4])
