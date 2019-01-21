class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = 0
        ans = 0
        while r < len(s):
            if s[r] in s[l:r]:
                idx = l+s[l:r].index(s[r])
                ans = max(ans, r-l)
                l = idx+1
            r = r + 1
            # print(l,r)
        ans = max(ans, r-l)
        return ans