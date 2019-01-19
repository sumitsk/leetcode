# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.maxDepth_bottom_up(root)
        # self.max_depth = 0
        # self.maxDepth_top_down(root, 0)
        # return self.max_depth
        
    def maxDepth_top_down(self, node, depth):
        # update max_depth if leaf node
        if node is None:
            self.max_depth = max(depth, self.max_depth)
        else:
            self.maxDepth_top_down(node.left, depth+1)
            self.maxDepth_top_down(node.right, depth+1)
        
    def maxDepth_bottom_up(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.maxDepth_bottom_up(node.left), self.maxDepth_bottom_up(node.right))