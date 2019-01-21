class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = set([x for x in J])
        count = 0
        for c in S:
            if c in jewels:
                count += 1
        return count