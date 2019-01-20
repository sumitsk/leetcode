# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        node = root
        parent = None
        # search for the appropriate leaf node
        while node is not None:
            prev_node = node
            if node.val < val:
                node = node.right
            else:
                node = node.left
        new_node = TreeNode(val)
        if val < prev_node.val:
            prev_node.left = new_node
        else:
            prev_node.right = new_node
        return root