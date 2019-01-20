# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.lca = None
        self.search_lca(root, p, q)
        return self.lca
    
    def search_lca(self, node, p, q):
        if self.lca is not None:
            return 
        if node is None:
            return 
        
        # search for q
        if node.val == p.val:
            if self.in_subtree(node, q.val):
                self.lca = node
                return 
            else:
                return True
            
        # search for p
        elif node.val == q.val:
            if self.in_subtree(node, p.val):
                self.lca = node
                return 
            else:
                return True
        
        # search deeper
        else:
            left_res = self.search_lca(node.left, p, q)
            right_res = self.search_lca(node.right, p, q)
            if left_res and right_res and self.lca is None:
                self.lca = node
                return 
            if left_res or right_res:
                return True
        
        
    def in_subtree(self, node, val):
        # return True if val is in the subtree of node
        if node is not None:
            if node.val == val:
                return True
            elif node.val < val:
                return self.in_subtree(node.right, val)
            else:
                return self.in_subtree(node.left, val)
            