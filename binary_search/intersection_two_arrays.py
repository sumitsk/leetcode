class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = self.mergesort(nums1)
        nums2 = self.mergesort(nums2)
        res = []
        i=j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                if len(res)==0 or res[-1]!=nums1[i]:
                    res.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return res

    def mergesort(self, arr):
        if len(arr)<=1:
            return arr
        mid = len(arr)//2
        left = self.mergesort(arr[:mid])
        right = self.mergesort(arr[mid:])
        return self.merge_sorted(left, right)

    def merge_sorted(self, left, right, return_idx=False):
        arr=[0]*(len(left)+len(right))
        if return_idx:
            idx = [0]*(len(left)+len(right))
        # merge left and right sorted halves
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                arr[k]=left[i]
                if return_idx:
                    idx[k]=0
                i+=1
            else:
                arr[k]=right[j]
                if return_idx:
                    idx[k]=1
                j+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            if return_idx:
                idx[k]=0
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            if return_idx:
                idx[k]=1
            j+=1
            k+=1
        if return_idx:
            return arr, idx
        return arr


sol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
sol.intersection(nums1, nums2)        