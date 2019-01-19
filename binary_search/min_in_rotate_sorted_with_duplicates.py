class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # duplicates can not be handled with O(logn) complexity
        # eg. [2,2,2,2,2,2,2,2,2,2,2,2,2,0,2] - it is not possible to do a binary search
        return min(nums)