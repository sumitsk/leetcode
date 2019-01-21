class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = dict([(n,0) for n in nums])
        for n in nums:
            count[n] += 1
            
        # find top k frequent elements from count
        unique = list(count.keys())
        freq = [count[u] for u in unique]
        self.mergesort_with_index(freq, unique)
        return unique[-k:]
        
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