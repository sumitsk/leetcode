# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # return self.issymmetric_recursive(root, root)
        return self.issymmetric_iterative(root)
        
        
    def issymmetric_recursive(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is not None and node2 is not None:
            if node1.val == node2.val:
                ans1 = self.issymmetric_recursive(node1.left, node2.right)
                ans2 = self.issymmetric_recursive(node1.right, node2.left)
                return ans1 and ans2
        return False
        
    def valid_nodes(self, node1, node2):
        if node1.val != node2.val:
            return False
        if node1.left is not None and node2.right is None :
            return False
        if node1.left is None and node2.right is not None :
            return False
        if node1.right is not None and node2.left is None:
            return False
        if node1.right is None and node2.left is not None:
            return False
        return True
        
    def try_left(self, node):
        return node.left is not None
    
    def try_right(self, node):
        return node.right is not None
    
    def move_left_right(self, node1, node2):
        prev_node1, prev_node2 = node1, node2
        node1 = node1.left
        node2 = node2.right
        return prev_node1, prev_node2, node1, node2
    
    def move_right_left(self, node1, node2):
        prev_node1, prev_node2 = node1, node2
        node1 = node1.right
        node2 = node2.left
        return prev_node1, prev_node2, node1, node2
    
    def move_up(self, node1, node2):
        prev_node1, prev_node2 = node1, node2
        node1 = node1.parent
        node2 = node2.parent
        return prev_node1, prev_node2, node1, node2
        
    def issymmetric_iterative(self, root):
        if root is None:
            return True
        node1, node2 = root, root
        prev_node1, prev_node2 = None, None
        done = False
        while not done:
            if node1 is not None and node2 is not None:
                if self.valid_nodes(node1, node2):
                    # visiting first time
                    if not hasattr(node1, 'parent'):
                        node1.parent = prev_node1
                        node2.parent = prev_node2
                        if self.try_left(node1):
                            prev_node1, prev_node2, node1, node2 = self.move_left_right(node1, node2)
                        elif self.try_right(node1):
                            prev_node1, prev_node2, node1, node2 = self.move_right_left(node1, node2)
                        else:
                            prev_node1, prev_node2, node1, node2 = self.move_up(node1, node2)
                            
                    # node already visited
                    else:
                        if prev_node1 is not node1.right and self.try_right(node1):
                            prev_node1, prev_node2, node1, node2 = self.move_right_left(node1, node2)
                        else:
                            prev_node1, prev_node2, node1, node2 = self.move_up(node1, node2)
                else:
                    return False
            elif node1 is None and node2 is None:
                    return True
            else:
                return False
            done = node1 is root and node2 is root
        return True