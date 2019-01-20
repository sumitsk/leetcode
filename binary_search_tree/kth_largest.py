class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.mergesort(nums)
        self.arr = nums[-k:]

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """

        # insert val in the sorted array
        self.insert_sorted(val)
        self.arr = self.arr[-self.k:]
        # kth element from back
        ans = self.arr[0]
        return ans

    def mergesort(self, arr):
        if len(arr)>1:
            mid = len(arr)//2
            left, right = arr[:mid], arr[mid:]
            self.mergesort(left)
            self.mergesort(right)
            # left and right subarrays are sorted, now merge them
            i = j = t = 0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    arr[t] = left[i]
                    i += 1 
                else:
                    arr[t] = right[j]
                    j += 1
                t += 1
            while i<len(left):
                arr[t] = left[i]
                i += 1
                t += 1
            while j<len(right):
                arr[t] = right[j]
                t += 1
                j += 1


    def find_index(self, val):
        # index at which val will be inserted in the sorted array
        arr = self.arr
        if len(arr)==0 or val<arr[0]:
            return 0
        elif val>arr[-1]:
            return len(arr)

        left, right = 0, len(arr)-1
        while left<right-1:
            mid = (left+right)//2
            if arr[mid]<val:
                left = mid
            else:
                right = mid
        a1, b1 = min(left, right), max(left, right)
        return (b1+1 if arr[b1]<=val else a1+1)

    def insert_sorted(self, val):
        # insert val in the sorted array arr
        idx = self.find_index(val)
        self.arr = self.arr[:idx] + [val] + self.arr[idx:]


# Your KthLargest object will be instantiated and called as such:
k = 7
nums = [-10,1,3,1,4,10,3,9,4,5,1]
new = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
obj = KthLargest(k, nums)

# k = 3
# nums = [4,5,8,2]
# new = [3,5,10,9,4]
for n in new:
    a = obj.add(n)
    print(a)

