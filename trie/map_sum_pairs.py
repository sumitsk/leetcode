class Node:
    def __init__(self):
        # assuming only lower case alphabets
        self.children = [None]*26
        self.val = None
        
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        node = self.root
        for ch in key:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Node()
            node = node.children[idx]
        node.val = val
        
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Node()
            node = node.children[idx]
        # check all the subtrees 
        sumval = self.recur(node)
        return sumval
        
    def recur(self, node):
        if node is None:
            return 0
        val = node.val if node.val is not None else 0
        for ch in node.children:
            val += self.recur(ch)
        return val

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)