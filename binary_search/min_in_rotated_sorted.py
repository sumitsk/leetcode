class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        n = len(nums)
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if (mid==0 or nums[mid-1]>nums[mid]) and (mid==n-1 or nums[mid+1]>nums[mid]):
                return nums[mid]
            else:
                if nums[mid]>nums[r]:
                    l=mid+1
                else:
                    r=mid-1