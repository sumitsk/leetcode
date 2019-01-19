# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        self.path_sums = []
        self.find_path_sums(root, 0)
        if sum in self.path_sums:
            return True
        return False
        
    def find_path_sums(self, node, path_sum):
        # leaf node
        if node.left is None and node.right is None:
            self.path_sums.append(path_sum + node.val)
        if node.left is not None:
            self.find_path_sums(node.left, path_sum + node.val)
        if node.right is not None:
            self.find_path_sums(node.right, path_sum + node.val)
        