"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        self.postorder_recursive(root, res)
        return res
        
    def postorder_recursive(self, node, res):
        if node is not None:
            for child in node.children:
                self.postorder_recursive(child, res)
            res.append(node.val)
