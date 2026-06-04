# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
- binary search tree -> number on the left is less, right is more 
- at a current node: 
    - if the given node values are both less, there might be 
        an ancestor down the line 
    - if the values are greater than the current node, there might 
        be  more common ancestor down the line 
- base case: 
    if the left and the right sub child match p and q, then you are 
    the lowest common ancestor 

'''
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if p.val < root.val and q.val < root.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val: 
            return self.lowestCommonAncestor(root.right, p, q)
        else: 
            return root


        