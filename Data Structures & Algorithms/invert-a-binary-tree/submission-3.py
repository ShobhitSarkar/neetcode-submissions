# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
what's the base case: 
    - if a node is None, return none 
what do I need from children: 
    -  invert their trees 
how to combine:
    - make the right subtree left 
    - make the left sub tree right 
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root == None: 
            return None 

        inverted_left = self.invertTree(root.left)
        inverted_right = self.invertTree(root.right)

        root.left = inverted_right 
        root.right = inverted_left

        return root 
        