# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # iterative solution has been implemented in some other file
        ans = []
        self.recur(root, ans)
        return ans
    
    def recur(self, node, ans):
        if node is not None:
            self.recur(node.left, ans)
            ans.append(node.val)
            self.recur(node.right, ans)
        