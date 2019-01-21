class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dct = {}
        for i,n in enumerate(nums):
            if n in dct:
                if i-dct[n][-1] <=k:
                    return True
                dct[n].append(i)
            else:
                dct[n]=[i]
        return False