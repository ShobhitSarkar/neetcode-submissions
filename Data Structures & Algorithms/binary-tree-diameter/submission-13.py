# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
tidbits: 
    - diameter = left_height + right_height 
    
recursive algorithm for height: 
    - if the root is none, return 0 
    - recursivel calculate height for left & right, 
    - add one for yourself to the max between left & right heights 

putting it together: 
    - instantiate a result variable
    - in recursive, update the max_diameter as max between left+right_height 
        and the max_diameter 
    - return the max_diameter 
'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.max_diameter = 0 

        def height(node): 
            """
            helper method to calculate the height of the tree 
            """

            if node == None: 
                return 0 

            left_height = height(node.left)
            right_height = height(node.right)

            self.max_diameter = max(self.max_diameter, left_height + right_height)

            return 1 + max(left_height, right_height)

        
        height(root)

        return self.max_diameter
        