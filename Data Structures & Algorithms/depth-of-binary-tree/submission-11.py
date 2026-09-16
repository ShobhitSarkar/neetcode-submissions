# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
-- from a particular node's perspective, what does it need: 
    - it needs the height of it's sub tree, compare it & then add one to itself + return 

"""


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        