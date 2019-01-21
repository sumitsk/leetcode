class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dct = {}
        for s in strs:
            key = self.get_key(s)
            if key in dct:
                dct[key].append(s)
            else:
                dct[key] = [s]
        return [dct[k] for k in dct]
        
    def get_key(self, s):
        # all lowercase letters
        key = [0]*26
        for ch in s:
            key[ord(ch)-ord('a')] +=1 
        return ''.join([str(s) for s in key])
        