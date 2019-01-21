class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        self.mergesort(nums1)
        self.mergesort(nums2)
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
        if len(arr)>1:
            mid = len(arr)//2
            left, right = arr[:mid], arr[mid:]
            self.mergesort(left)
            self.mergesort(right)
            i = j = k =0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    arr[k] = left[i]
                    i +=1 
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            while i<len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j<len(right):
                arr[k] = right[j]
                j += 1
                k += 1
    