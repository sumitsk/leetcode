class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        n = len(str)
        all_ints = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        all_symbs = ['-', '+']
        while i<n and str[i]==' ':
            i += 1
        if i==n:
            return 0
        
        first = str[i]
        if not (first in all_symbs or first in all_ints):
            return 0
        
        neg = False
        if first == '-':
            i += 1
            neg = True
        elif first == '+':
            i += 1
            
        # read all integers here
        j = i
        while i<n and str[i] in all_ints:
            i += 1
        val = self.to_int(str[j:i])
        if neg:
            val = -val
        val = min(2**31-1, max(-2**31,val))
        return val
        
    def to_int(self, lst):
        val = 0
        c = 1
        for x in reversed(lst):
            val = val + c*int(x)
            c = c * 10
        return val          
        
sol = Solution()
str = '42'
ans = sol.myAtoi(str)
print(ans)