# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
base case: 
    - if you're a node then height is 1 
what do I need from my children: 
    - maximum of their heights 
how to combine: 
    - 1 (myself) + max height of my children 
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None: 
            return 0 
        
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        return 1 + max(left_height, right_height)
        