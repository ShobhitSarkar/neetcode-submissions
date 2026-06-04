# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
comaprisons 

if both are none: they're the same: 
    - return True 

if one is none other is not: not the same 
    - return False 

if both exists: 
    - if value same -> true 
    - if values not same -> false 

putting them together: 
    - p's and q's left sub trees need to be checked 
    - p's and q's right sub trees need to be checked 

'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p == None and q == None: 
            return True 
        
        if p is None or q is None: 
            return False 

        if p.val != q.val: 
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        