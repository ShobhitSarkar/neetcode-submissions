# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
traverse through both of the trees - any order 
if at any point, the values don't match - then return false 
'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        ## both empty 
        if p == None and q == None: 
            return True 

        ## one empty one is not 
        if p is None or q is None:
            return False 

        ## both exist 
        if p.val != q.val:
            return False
        
        ## recurse on children 
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        