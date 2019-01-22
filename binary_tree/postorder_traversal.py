# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        # self.postorder_recursive(root, res)
        self.postorder_iterative(root, res)
        return res
        
    def postorder_recursive(self, root, res):
        if root is not None:
            self.postorder_recursive(root.left, res)
            self.postorder_recursive(root.right, res)        
            res.append(root.val)
    
    def postorder_iterative(self, root, res):
        node = root
        prev_node = None
        while node is not None:
            # node visited first time
            if not hasattr(node, 'parent'):
                node.parent = prev_node
                prev_node = node
                if node.left is not None:
                    node = node.left
                elif node.right is not None:
                    node = node.right
                elif node.parent is not None:
                    res.append(node.val)
                    node = node.parent
                else:
                    res.append(node.val)
                    return
                
            # move to right
            elif prev_node == node.left:
                prev_node = node
                if node.right is not None:
                    node = node.right
                elif node.parent is not None:
                    res.append(node.val)
                    node = node.parent
                else:
                    res.append(node.val)
                    return
                
            # move to parent
            elif prev_node == node.right:
                res.append(node.val)
                prev_node = node
                node = node.parent
            else:
                res.append(node.val)
                return    