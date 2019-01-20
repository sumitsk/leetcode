# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.recurse(nums)    
        return root
    
    def recurse(self, nums):
        if len(nums)>0:
            mid = len(nums)//2
            node = TreeNode(nums[mid])
            node.left = self.recurse(nums[:mid])
            node.right = self.recurse(nums[mid+1:])
            return node
            