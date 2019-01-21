class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # worst case complexity O(n^2)
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in nums[i+1:]:
        #         return [i,nums[i+1:].index(diff)+i+1]
            
        # complexity O(nlogn)
        idx = list(range(len(nums)))
        self.mergesort_with_index(nums, idx)
        l = 0
        r = len(nums)-1
        while l<r:
            sum_ = nums[l] + nums[r]
            if sum_==target:
                return [idx[l], idx[r]]
            elif sum_ < target:
                l += 1
            else:
                r -= 1
        
    def mergesort_with_index(self, arr, idx):
        if len(arr)>1:
            mid = len(arr)//2
            left, right = arr[:mid], arr[mid:]
            li, ri = idx[:mid], idx[mid:]
            self.mergesort_with_index(left, li)
            self.mergesort_with_index(right, ri)
            i = j = k =0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    arr[k] = left[i]
                    idx[k] = li[i]
                    i +=1 
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
                
                