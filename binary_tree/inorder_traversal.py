# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        # self.inorder_recursive(root, res)
        self.inorder_iterative(root, res)
        return res
        
    def inorder_recursive(self, root, res):
        if root is not None:
            self.inorder_recursive(root.left, res)
            res.append(root.val)
            self.inorder_recursive(root.right, res)
            
    
    def inorder_iterative(self, root, res):
        node = root
        prev_node = None
        while node is not None:
            # node visited first time
            if not hasattr(node, 'parent'):
                node.parent = prev_node
                prev_node = node
                # move left
                if node.left is not None:
                    node = node.left
                else:
                    res.append(node.val)
                    # move right if left child does not exist
                    if node.right is not None:
                        # res.append(node.val)
                        node = node.right
                    # leaf node
                    elif node.parent is not None:
                        # res.append(node.val)
                        node = node.parent
                    else:
                        return
                
            # move to right
            elif prev_node == node.left:
                res.append(node.val)
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