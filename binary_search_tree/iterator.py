# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # generator object 
        self.gen = self.traversal(root)
        self.largest_elem = self.find_largest(root)
        self.last_elem = None

    def find_largest(self, root):
        if root is None:
            return None
        node = root
        while node.right is not None:
            node = node.right
        return node.val

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        next_elem = next(self.gen)
        self.last_elem = next_elem
        return next_elem

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.largest_elem is not None and self.last_elem != self.largest_elem:
            return True
        return False
    
    def traversal(self, node):
        if node is not None:
            for x in self.traversal(node.left):
                yield x
            yield node.val
            for x in self.traversal(node.right):
                yield x


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()