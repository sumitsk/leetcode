# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)==0:
            return None
        if len(inorder)==1:
            node = TreeNode(inorder[0])
            return node
        
        # find the root node
        root = TreeNode(postorder[-1])
        # partition inorder and postorder lists
        idx = inorder.index(root.val)
        left_tree = self.buildTree(inorder[:idx], postorder[:idx])
        right_tree = self.buildTree(inorder[idx+1:], postorder[idx:-1])
        root.left = left_tree
        root.right = right_tree
        return root