# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        res = self.delete(root, key)
        return res
    
    def delete(self, node, key):
        if node is not None:
            # search in the right subtree
            if node.val < key:
                node.right = self.delete(node.right, key)
                return node

            # search in the left subtree
            elif node.val > key:
                node.left = self.delete(node.left, key)
                return node
                
            # node found
            else:
                if node.left is None:
                    return node.right
                    
                elif node.right is None:
                    return node.left
        
                # node has both children
                else:
                    # find inorder successor
                    temp = node.right
                    while temp.left is not None:
                        temp = temp.left
                    node.val = temp.val
                    # delete inorder successor
                    node.right = self.delete(node.right, temp.val)
                    return node
                
                