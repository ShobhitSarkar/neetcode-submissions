# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
base case / operation: 
    - invert the left and the right node 
what do I need from children: 
    - tell my right and left sub tree toinvert themselves 
'''

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root == None: 
            return root

        inverted_left = self.invertTree(root.left)
        inverted_right = self.invertTree(root.right)

        root.left = inverted_right 
        root.right = inverted_left 

        return root
        