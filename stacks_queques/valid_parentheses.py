class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        x = []
        open_bracs = ['(', '{', '[']
        closed_bracs = [')', '}', ']']
        for ch in s:
            if ch in open_bracs:
                x.append(ch)
            else:
                if len(x)==0:
                    return False
                c = x.pop()
                if open_bracs.index(c)!=closed_bracs.index(ch):
                    return False
        if len(x)!=0:
            return False
        return True
            