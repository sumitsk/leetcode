
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        lst = [[] for _ in range(numRows)]
        i = 0
        inc = +1
        for ch in s:
            lst[i].append(ch)
            i += inc
            if i==numRows:
                inc = -1
                i = numRows-2
            elif i==-1:
                inc = +1
                i = 1

        final_lst = sum(lst, [])
        st = ''.join(final_lst)
        return st

sol = Solution()
s = 'ABC'
numRows = 2
ans = sol.convert(s, numRows)
print(ans)
