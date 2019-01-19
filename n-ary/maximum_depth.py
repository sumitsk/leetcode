"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        child_depths = [self.maxDepth(child) for child in root.children]
        max_depth = 0 if len(child_depths)==0 else max(child_depths)
        return 1 + max_depth
    