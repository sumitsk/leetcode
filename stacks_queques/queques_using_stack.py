class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.data.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        # violating stacks
        # return self.data.pop(0)
        
        # stack can only access the topmost element
        backup = []
        while not self.empty():
            backup.append(self.data.pop())
        self.data = list(reversed(backup[:-1]))
        return backup[-1]

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        # violating stacks
        # return self.data[0]
        
        # stack can only access the topmost element
        backup = []
        while not self.empty():
            backup.append(self.data.pop())
        self.data = list(reversed(backup))
        return backup[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.data)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()