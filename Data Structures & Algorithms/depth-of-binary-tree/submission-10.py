# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
high level algorithm: 
    - add one for current node, take the max between 
    the left sub tree & right sub tree 
    - base case: 
        - if the root is none, then return 0 
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None: 
            return 0 

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        return 1 + max(left_height, right_height)
        