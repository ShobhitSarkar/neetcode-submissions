# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
base case: 
    - if the node is none, return None 

what do I need from my children: 
    - the max between their diameters 

how do I combine: 
    - 
'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        ## global store for keeping track of the diameter
        self.res = 0 

        ## return the height (return value is not the result)
        def dfs(curr): 
            if not curr: 
                return 0 

            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)

            return 1 + max(left, right)

        dfs(root)

        return self.res

