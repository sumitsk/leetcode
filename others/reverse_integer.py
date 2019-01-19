class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        lst = []
        inp = abs(x)
        while inp!=0:
            digit = inp%10
            lst.append(digit)
            inp = inp//10
        val = self.to_int(lst)
        if x < 0:
            val = - val
        return val
        
    def to_int(self, lst):
        val = 0
        c = 1
        for x in reversed(lst):
            val = val + c*x
            c = c * 10
        return val

sol = Solution()
x = -123
ans = sol.reverse(x)
print(ans)