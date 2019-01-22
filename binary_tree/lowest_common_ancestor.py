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
        self.recurse(root, p, q)
        return self.lca
    
    def recurse(self, node, p, q):
        if self.lca is None and node is not None:
            if node.val == p.val:
                if self.in_subtree(node, q):
                    self.lca = node
                    return
                return True
            elif node.val == q.val:
                if self.in_subtree(node, p):
                    self.lca = node
                    return 
                return True
            else:
                left_res = self.recurse(node.left, p, q)
                right_res = self.recurse(node.right, p, q)

                if left_res and right_res:
                    self.lca = node
                elif left_res or right_res:
                    return True
        
    def in_subtree(self, node, p):
        if node is not None:
            if node.val == p.val:
                return True
            l = self.in_subtree(node.left, p)
            r = self.in_subtree(node.right, p)
            return l or r
        return False