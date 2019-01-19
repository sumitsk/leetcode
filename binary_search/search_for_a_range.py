class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = self.find_leftindex(nums, target)
        r = self.find_rightindex(nums, target)
        return [l,r]
        
    def find_leftindex(self, nums, target):
        l = 0
        n = len(nums)
        r = n - 1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target and (mid==0 or nums[mid-1]<nums[mid]):
                return mid
            elif nums[mid]>=target:
                r=mid-1
            else:
                l=mid+1                
        return -1
        
    def find_rightindex(self, nums, target):
        l = 0
        n = len(nums)
        r = n - 1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target and (mid==n-1 or nums[mid+1]>nums[mid]):
                return mid
            elif nums[mid]<=target:
                l=mid+1
            else:
                r=mid-1                
        return -1