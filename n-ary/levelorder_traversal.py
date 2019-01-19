"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        openlist = [root]
        res = [[root.val]]
        while len(openlist)>0:
            n = len(openlist)
            next_lvl = []
            for i in range(n):
                node = openlist[i]
                for child in node.children:
                    if child is not None:
                        openlist.append(child)
                        next_lvl.append(child.val)
            openlist = openlist[n:]
            if len(next_lvl)>0:
                res.append(next_lvl)
        return res