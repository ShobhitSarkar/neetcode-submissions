# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
if the root is none: 
    - return 0 

base case: 
    - need the maximum depth between left and right sub tree 
    - add 1 for "my" height 

- do the same for left and right sub tree 
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None: 
            return 0

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        return 1 + max(left_height, right_height)


        