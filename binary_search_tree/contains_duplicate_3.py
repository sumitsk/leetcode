class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        idx = list(range(len(nums)))
        self.mergesort_with_index(nums, idx)
        left = 0
        right = 1
        while left<len(nums) and right<len(nums):
            if nums[right] - nums[left] <= t:
                if abs(idx[right]-idx[left])<=k:
                    return True
                else:
                    right += 1
            else:
                left += 1
                if left==right:
                    right += 1
        return False

    def mergesort_with_index(self, arr, idx):
        if len(arr)>1:
            mid = len(arr)//2
            left, right = arr[:mid], arr[mid:]
            li, ri = idx[:mid], idx[mid:]
            
            self.mergesort_with_index(left, li)
            self.mergesort_with_index(right, ri)
            
            i = j = k = 0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    arr[k] = left[i]
                    idx[k] = li[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    idx[k] = ri[j]
                    j += 1
                k += 1
            while i<len(left):
                arr[k] = left[i]
                idx[k] = li[i]
                i += 1
                k += 1
                
            while j<len(right):
                arr[k] = right[j]
                idx[k] = ri[j]
                j += 1
                k += 1