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
        # self.connect_levelsearch(root)
        # self.connect_recur(root)
        self.connect_iterative(root)
        
    def connect_iterative(self, root):
        # true O(1) extra space
        leftmost = root
        while leftmost is not None:
            curr = leftmost
            while curr is not None:
                if curr.left is not None:
                    curr.left.next = curr.right
                    curr.right.next = curr.next.left if curr.next is not None else None
                curr = curr.next
            leftmost = leftmost.left
        
    def connect_levelsearch(self, root):
        # uses O(logn) extra space
        if root is None:
            return
        # run a level order search 
        openlist = [root]
        while len(openlist) > 0:
            n = len(openlist)
            openlist.append(None)
            for i in range(n):
                node = openlist[i]
                node.next = openlist[i+1]
                if node.left is not None:
                    openlist.append(node.left)
                if node.right is not None:
                    openlist.append(node.right)
            openlist = openlist[n+1:]
            
    def connect_recur(self, root):
        # recursive approach uses implicit extra space
        if root is None:
            return
        root.next = None
        self.recur(root)
            
    def recur(self, node):
        # constant extra space
        if node is not None:
            if node.left is not None:
                node.left.next = node.right
                if node.next is not None:
                    node.right.next = node.next.left
            self.recur(node.left)
            self.recur(node.right)
    
           
        