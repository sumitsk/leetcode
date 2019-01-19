class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        n = len(nums)
        if n==1:
            return 0
        r = n-1
        while l<=r:
            mid = (l+r)//2
            if (mid==0 or nums[mid-1]<nums[mid]) and (mid==n-1 or nums[mid]>nums[mid+1]):
                return mid
            elif mid>0 and nums[mid-1]>nums[mid]:
                r = mid-1
            else:
                l = mid+1