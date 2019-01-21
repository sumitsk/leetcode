class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dct = {}
        for ch in s:
            dct[ch]=dct[ch]+1 if ch in dct else 1
        for i,ch in enumerate(s):
            if dct[ch]==1:
                return i
        return -1