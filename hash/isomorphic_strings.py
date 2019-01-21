class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        n = len(s)
        hashmap = {}
        vals = set()
        for i in range(n):
            key, val = s[i], t[i]
            if key not in hashmap:
                if val not in vals: 
                    hashmap[key]=val
                    vals.add(val)
                else:
                    return False
            elif hashmap[key]!=val:
                return False
        return True