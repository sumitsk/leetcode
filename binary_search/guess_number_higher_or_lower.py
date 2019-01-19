class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l<r:
            mid = (l+r)//2
            ans = guess(mid)
            if ans==0:
                return mid
            elif ans==-1:
                r = mid-1
            else:
                l = mid+1
        return l        