class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # using extra memory
        hashset = set()
        for n in nums:
            if n not in hashset:
                hashset.add(n)
            else:
                hashset.remove(n)
        return [x for x in hashset][0]
            
        