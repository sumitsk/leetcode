class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.k = k
        self.queque = [None]*k
        self.head = None
        self.tail = None

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if self.tail is None:
            self.head = 0
            self.tail = 0
        self.queque[self.tail] = value
        self.tail = (self.tail+1)%self.k
        return True
        
    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.head = (self.head+1)%self.k
        if self.head == self.tail:
            self.head=None
            self.tail=None
        return True
        
    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        
        if self.isEmpty():
            return -1
        return self.queque[self.head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queque[(self.tail-1)%self.k]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.head is None:
            return True
        return False

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if self.head is not None and self.tail==self.head:
            return True
        return False
        
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()