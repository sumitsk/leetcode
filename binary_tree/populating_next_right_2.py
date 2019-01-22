# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        self.connect_iterative(root)
        
    def connect_iterative(self, root):
        # leftmost node at each level
        leftmost = root
        while leftmost is not None:
            curr = leftmost
            while curr is not None:
                if curr.left is not None:
                    if curr.right is not None:
                        curr.left.next = curr.right
                        curr.right.next = self.find_next_right(curr.next)
                    else:
                        curr.left.next = self.find_next_right(curr.next)
                elif curr.right is not None:
                    curr.right.next = self.find_next_right(curr.next)
                curr = curr.next
            leftmost = self.find_next_right(leftmost)
        
    def find_next_right(self, node):
        # find next right node on the same level
        temp = node
        while temp is not None:
            if temp.left is not None:
                return temp.left
            if temp.right is not None:
                return temp.right
            temp = temp.next
        return None