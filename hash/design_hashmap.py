class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_buckets = 100
        self.buckets = [{} for _ in range(self.num_buckets)]

    def hash_func(self, key):
        return key%self.num_buckets
        
    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        m = self.hash_func(key)
        self.buckets[m][key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        m = self.hash_func(key)
        if key in self.buckets[m]:
            return self.buckets[m][key]
        return -1
    
    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        m = self.hash_func(key)
        if key in self.buckets[m]:
            del self.buckets[m][key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)