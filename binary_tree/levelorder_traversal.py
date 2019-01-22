# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        # nodes in the last level
        openlist = [root]
        while len(openlist) > 0:
            n = len(openlist)
            res.append([x.val for x in openlist])
            for i in range(n):
                node = openlist[i]
                if node.left is not None:
                    openlist.append(node.left)
                if node.right is not None:
                    openlist.append(node.right)
            openlist = openlist[n:]    
        return res 