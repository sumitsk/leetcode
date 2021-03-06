# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.ans = None
        self.traverse(root)
        return self.ans != False
        
    def traverse(self, node):
        if node is None:
            return 0
        
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        if abs(left - right) > 1:
            self.ans = False
        return max(left, right)+1
        