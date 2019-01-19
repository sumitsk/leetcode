"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        self.preorder_recursive(root, res)
        return res
        
    def preorder_recursive(self, node, res):
        if node is not None:
            res.append(node.val)
            for child in node.children:
                self.preorder_recursive(child, res)
                
        