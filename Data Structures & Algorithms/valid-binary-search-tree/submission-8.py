# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
for every node: 
    - check whether left value is lesser 
    - right value is greater than node 

basically: left node is the min value, right node is the max value 

- for every node, we need to compare whether the node val falls in that range 
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, min_value, max_value): 

            if not node: 
                return True 

            if node.val <= min_value or node.val >= max_value: 
                return False 

            ## left child must be less than current node
            ## right child must be greater than current node 
            return dfs(node.left, min_value, node.val) and dfs(node.right, node.val, max_value)

        return dfs(root, float('-inf'), float('inf'))