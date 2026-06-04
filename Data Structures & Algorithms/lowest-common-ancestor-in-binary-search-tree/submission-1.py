# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
base case: 
    - when you've encountered the nodes themselves 
    - just return none if none 
what do I need from my children 
    - do you have the nodes that I am looking for? 
how do I put them back together: 
    - if both or either one of my sub trees come back with a yes 
    - then I am the lowest common ancestor 

'''
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if root is None: 
            return None 

        if root.val == p.val or root.val == q.val: 
            return root 

        left = self.lowestCommonAncestor(root.left, p, q )
        right = self.lowestCommonAncestor(root.right, p, q)

        if right and left: 
            return root 

        return left if left else right
