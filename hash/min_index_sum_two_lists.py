class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        h1 = {}
        for i, key in enumerate(list1):
            h1[key]=i
        min_idx_sum = len(list1) + len(list2)
        for i, rest in enumerate(list2):
            if rest in h1:
                idx_sum = h1[rest]+i
                if idx_sum<min_idx_sum:
                    min_idx_sum=idx_sum
                    ans=[rest]
                elif idx_sum==min_idx_sum:
                    ans.append(rest)
        return ans
        