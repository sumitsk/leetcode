class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        idx = self.closest_leftindex(arr, x)
        l = idx
        r = idx
        n = len(arr)
        while (r-l+1)!=k:
            # print(l,r)
            if r==n-1:
                l=l-1
            elif l==0:
                r=r+1
            elif abs(arr[l-1]-x)<=abs(arr[r+1]-x):
                l=l-1
            else:
                r=r+1
        return arr[l:r+1]
    
    def closest_leftindex(self, nums, target):
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
        # target not found in nums
        if l==0 or abs(nums[l]-target)<abs(nums[l-1]-target):
            return l
        else:
            return self.closest_leftindex(nums, nums[l-1])