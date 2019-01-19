class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0 or x==1:
            return x
        l = 0
        r = x-1
        while l<r:
            mid = (l+r)//2
            mid_sq = mid**2
            midp1_sq = mid_sq + 2*mid + 1
            if mid_sq > x:
                r = mid - 1
            elif mid_sq == x:
                return mid
            else:    
                if midp1_sq < x:
                    l = mid + 1
                elif midp1_sq == x:
                    return mid+1
                else:
                    return mid
        return l        
            