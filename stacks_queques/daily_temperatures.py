class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # read from the back of the list, store in a stack and pop out topmost element 
        # if the next entry is larger than that
        
        stack = []
        n = len(T)
        ans = [0]*n
        for i in reversed(range(n)):
            # pop elements from top smaller than the current element
            while len(stack)>0 and T[i]>=T[stack[-1]]:
                stack.pop()
            if len(stack)>0:
                ans[i] = stack[-1] - i
            
            stack.append(i)
                
            # ans[i] = count
        return ans
            