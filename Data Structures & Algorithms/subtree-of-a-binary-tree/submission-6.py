# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root == None: 
            return False
        
        if self.sameTree(root, subRoot): 
            return True 
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def sameTree(self, first_tree, second_tree): 
        
        if first_tree == None and second_tree == None: 
            return True 

        if first_tree == None or second_tree == None: 
            return False 

        if first_tree.val != second_tree.val: 
            return False 

        return self.sameTree(first_tree.left, second_tree.left) and self.sameTree(first_tree.right, second_tree.right)
        
        