# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)==0:
            return None
        if len(inorder)==1:
            node = TreeNode(inorder[0])
            return node
        
        # find the root node
        root = TreeNode(preorder[0])
        # partition inorder and postorder lists
        idx = inorder.index(root.val)
        left_tree = self.buildTree(preorder[1:idx+1], inorder[:idx])
        right_tree = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        root.left = left_tree
        root.right = right_tree
        return root