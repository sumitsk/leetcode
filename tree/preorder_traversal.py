# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        # self.preorder_recursive(root, res)
        self.preorder_iterative(root, res)
        return res
    
    def preorder_recursive(self, root, res):
        if root is not None:
            res.append(root.val)
            self.preorder_recursive(root.left, res)
            self.preorder_recursive(root.right, res)
            
    def preorder_iterative(self, root, res):
        node = root
        prev_node = None
        while node is not None:
            # node visited first time
            if not hasattr(node, 'parent'):
                res.append(node.val)
                node.parent = prev_node
                prev_node = node
                if node.left is not None:
                    node = node.left
                elif node.right is not None:
                    node = node.right
                elif node.parent is not None:
                    node = node.parent
                else:
                    return
                
            # move to right
            elif prev_node == node.left:
                prev_node = node
                if node.right is not None:
                    node = node.right
                elif node.parent is not None:
                    node = node.parent
                else:
                    return
                
            # move to parent
            elif prev_node == node.right:
                prev_node = node
                node = node.parent
            else:
                return