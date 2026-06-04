# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
if the root is none: 
    return none 

- we do a dfs:
    - only difference, at every step, we do a comparision on the 
    longest route passing through that node 
'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def height(node): 

            if not node: 
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            self.res = max(self.res, left_height+right_height)

            return 1 + max(left_height, right_height)

        height(root)

        return self.res



        