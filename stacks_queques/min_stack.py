class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.data)>0:
            self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.data)>0:
            return self.data[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.data)>0:
            return min(self.data)
        # enteries = []
        # while len(self.data) > 0: 
        #     enteries.append(self.top())
        #     self.pop()
        # if len(enteries)>0:
        #     ans = min(enteries)
        # else:
        #     ans = None
        # for et in reversed(enteries):
        #     self.push(et)
        # return ans
