# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- for a particular node, it needs the the left & right nodes exchanged 
    - extend that behavior to the entire sub trees 
- base case: 
    - if the root is none then return None 
- make a recursive call to invert left sub tree 
- make recursive call to invert right sub tree 
- switch them out 
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root == None: 
            return None 

        inverted_left = self.invertTree(root.left)
        inverted_right = self.invertTree(root.right)

        root.left = inverted_right 
        root.right = inverted_left 

        return root 
        