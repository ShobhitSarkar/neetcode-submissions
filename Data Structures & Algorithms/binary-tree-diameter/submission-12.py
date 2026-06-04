# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0 

        def height(node): 

            if node == None: 
                return 0 

            
            left_height = height(node.left)
            right_height = height(node.right)

            self.res = max(left_height + right_height, self.res)

            return 1 + max(left_height, right_height)

        height(root)

        return self.res
        