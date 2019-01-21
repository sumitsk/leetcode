class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hashset = set()
        while True:
            n = sum([int(s)**2 for s in str(n)])
            if n==1:
                return True
            if n in hashset:
                return False
            hashset.add(n)
            