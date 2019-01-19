# INCOMPLETE / UNSUCCESSFUL
# find median of two sorted arrays

import ipdb

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1)
        n2 = len(nums2)
        # special cases
        if n1==0:
            return self.median_sorted_array(nums2)
        if n2==0:
            return self.median_sorted_array(nums1)

        N = n1 + n2
        l1, r1 = 0, n1-1
        l2, r2 = 0, n2-1
        while True:
            idx1 = (l1+r1)//2
            # find index of largest element in nums2 smaller than v1
            idx2 = self.find_largest_elem(nums2[l2:r2+1], nums1[idx1])

            t2 = l2 + -1 if idx2 is None else idx2
            # arr1[idx1] is at index 'n' in the joint array
            n = idx1 + 1 + t2
            if n < N//2 - 1:
                # this should not be done if idx2 is None
                next_l1 = (l1+r1)//2
                next_l2 = (l2+r2)//2 if idx2 is not None else l2
                next_r1, next_r2 = r1, r2
            elif n == N//2 - 1:
                next_val = self.next_num(nums1, nums2, idx1, t2)
                if N%2==1:
                    return next_val
                else:
                    return (nums1[idx1] + next_val)/2
            elif n == N//2:
                if N%2==1:
                    return nums1[idx1]
                else:
                    prev_val = self.prev_num(nums1, nums2, idx1-1, t2)
                    return (prev_val + nums1[idx1])/2
            else:
                next_r1 = (l1+r1)//2
                next_r2 = (l2+r2)//2 if idx2 is not None else r2
                next_l1, next_l2 = l1, l2

            l1, l2, r1, r2 = next_l1, next_l2, next_r1, next_r2    
            # if (l1,l2,r1,r2) == (next_l1,next_l2,next_r1,next_r2):
            if r1-l1<=1 and r2-l2<=1:
                # ipdb.set_trace()
                # sort them until median index is reached
                if n<=N//2-1:
                    while n!=N//2-1:
                        idx1, t2, val = self.next_indices_and_num(nums1, nums2, idx1, t2)
                        n += 1
                    next_val = self.next_num(nums1, nums2, idx1, t2)
                    if N%2==1:
                        return next_val
                    else:
                        return (val + next_val)/2
                else:
                    while n!=N//2-1:
                        idx1, t2, next_val = self.prev_indices_and_num(nums1, nums2, idx1, t2)
                        n -= 1
                    if N%2==1:
                        return next_val
                    else:
                        val = self.prev_num(nums1, nums2, idx1, t2)
                        return (val + next_val)/2
            ipdb.set_trace()
        
    def median_sorted_array(self, arr):
        # median of a sorted array
        n = len(arr)
        if n%2==1:
            return arr[n//2]
        return (arr[n//2-1] + arr[n//2])/2    
        
    def find_largest_elem(self, arr, val):
        li = 0
        ri = len(arr)
        done = False
        while not done:
            if arr[(li+ri)//2] >= val:
                ri = (li+ri)//2
            else:
                li = (li+ri)//2
            done = li==ri or li+1==ri
        if arr[li]<val:
            return li
        return None

    def next_indices_and_num(self, arr1, arr2, idx1, idx2):
        if idx1>=len(arr1)-1:
            return idx1, idx2+1, arr2[idx2+1]
        if idx2>=len(arr2)-1:
            return idx1+1, idx2, arr1[idx1+1]
        if arr1[idx1+1] < arr2[idx2+1]:
            return idx1+1, idx2, arr1[idx1+1]
        else:
            return idx1, idx2+1, arr2[idx2+1]


    def prev_indices_and_num(self, arr1, arr2, idx1, idx2):
        if idx1<0:
            return idx1, idx2-1, arr2[idx2]
        if idx2<0:
            return idx1-1, idx2, arr1[idx1]
        if arr1[idx1] >= arr2[idx2]:
            return idx1-1, idx2, arr1[idx1]
        else:
            return idx1, idx2-1, arr2[idx2]
    
    
    def next_num(self, arr1, arr2, idx1, idx2):
        return self.next_indices_and_num(arr1, arr2, idx1, idx2)[-1]
    
    def prev_num(self, arr1, arr2, idx1, idx2):
        return self.prev_indices_and_num(arr1, arr2, idx1, idx2)[-1]

nums1 = [1]
nums2 = [2,3,4,5,6]
sol = Solution()
median = sol.findMedianSortedArrays(nums1, nums2)
print(median)

