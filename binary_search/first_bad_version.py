class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l<r:
            mid = (l+r)//2
            mid_is_bad = isBadVersion(mid)
            if mid_is_bad:
                r=mid
            else:
                l=mid+1
        return l