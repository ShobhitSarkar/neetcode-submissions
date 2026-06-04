# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
check every node, if there's a value that is greater than the parent, then it's a good node 
'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if root == None: 
            return -1 

        self.good_nodes = 0 

        def dfs(node, max_so_far): 

            if node == None: 
                return 

            if node.val >= max_so_far: 
                self.good_nodes += 1
            
            new_max = max(node.val, max_so_far)

            dfs(node.left, new_max)
            dfs(node.right, new_max)

        dfs(root, float('-inf'))

        return self.good_nodes