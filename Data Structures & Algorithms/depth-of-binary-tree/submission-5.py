# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
base case: 
- if a root is None, return None 

what do I need from children: 
- find the max between the height of the left sub tree and right sub tre 

how to combine: 
- add one for myself and then get the max of the left or right subtrees
'''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None: 
            return 0 

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        return 1 + max(left_height, right_height)
        