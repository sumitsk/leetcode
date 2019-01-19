class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        piv = self.pivot(nums)
        arr = nums[piv:] + nums[:piv]
        print(arr, piv)
        idx = self.search_sorted(arr, target)
        # print(arr, target, idx)
        if idx==-1:
            return -1
        return (idx+piv)%len(arr) 
        
    def search_sorted(self, arr, target):
        l = 0
        r = len(arr)-1
        while l<=r:
            # print(l,r)
            mid = (l+r)//2
            if arr[mid]<target:
                l = mid+1
            elif arr[mid]==target:
                return mid
            else:
                r = mid-1
        return -1
        
    def pivot(self, arr):
        l = 0
        r = len(arr)-1
        while l<=r:
            if (r-l)<=3:
                return l + arr[l:r+1].index(min(arr[l:r+1]))
            mid = (l+r)//2
            # expected - arr[l]<arr[mid]<arr[r]
            if arr[l]<arr[mid]<arr[r]:
                return l
            elif arr[l]>arr[mid]:
                r = mid
            else:
                l = mid  