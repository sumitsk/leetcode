# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.recur(root)
        
    def recur(self, node):
        if node is None:
            return True
        left_valid = self.recur(node.left)
        right_valid = self.recur(node.right)
        if left_valid and right_valid:
            if (node.left is None or node.val > node.left.max) and (node.right is None or node.val < node.right.min):
                node.min = node.left.min if node.left is not None else node.val
                node.max = node.right.max if node.right is not None else node.val
                return True
        return False