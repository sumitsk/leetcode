class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # dynamic programming
        res = list(range(n+1))
        for i in range(4, n+1):
            x = 1
            while x**2 <= i:
                res[i] = min(res[i], 1+res[i-x**2])
                x+=1 
        return res[n]


sol = Solution()
ans = sol.numSquares(7168)
print(ans)