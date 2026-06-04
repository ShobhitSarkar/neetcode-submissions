# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
base case: 
- take the left and make it into right 
- vice versa 

what do I need from children 
- they also need to do the same 

how do I em put em back together 
- don't need to do something 
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
        
        