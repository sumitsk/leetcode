class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_buckets = 100
        self.buckets = [[] for _ in range(self.num_buckets)]
        
    def hash_func(self, inp):
        return inp%self.num_buckets

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        m = self.hash_func(key)
        # avoid duplicates
        if key not in self.buckets[m]:        
            self.buckets[m].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        m = self.hash_func(key)
        if self.contains(key):
            self.buckets[m].remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        m = self.hash_func(key)
        if key in self.buckets[m]:
            return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)