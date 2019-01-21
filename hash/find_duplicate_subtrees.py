# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        hashmap = {}
        ans = []
        self.scan(root, hashmap, ans)
        return ans
        
    def scan(self, node, hashmap, ans):
        if node is not None:
            # serialize left and right subtree
            left_ser = self.scan(node.left, hashmap, ans)
            right_ser = self.scan(node.right, hashmap, ans)
            # node_ser = self.serialize(left_ser, right_ser, node)
            node_ser = '('+left_ser+str(node.val)+right_ser+')'
            if node_ser in hashmap:
                hashmap[node_ser] += 1
                if hashmap[node_ser]==2:
                    ans.append(node)
            else:
                hashmap[node_ser] = 1

            return node_ser
        return ""
