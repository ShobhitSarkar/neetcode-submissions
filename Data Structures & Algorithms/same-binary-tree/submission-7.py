# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
conditions for equivalency: 
    - if left & right are none: return True 
    - if left is None and right is not, return false (vice versa)
    - if left and right values are different: return false 
    - return true if the values are equal 

- build all of those out into a recursive check 
- run the check on the left sub trees and the right sub trees
    & left sub tree of the right, right subtree of the left 
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None: 
            return True 

        if p is None or q is None: 
            return False 
        
        if p.val != q.val: 
            return False 

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        