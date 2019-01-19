class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==0 or num==1:
            return True
        l = 1
        r = num-1
        while l<=r:
            mid = (l+r)//2
            mid_sq = mid**2
            if mid_sq == num:
                return True
            elif mid_sq < num:
                l = mid+1
            else:
                r = mid-1
        return False