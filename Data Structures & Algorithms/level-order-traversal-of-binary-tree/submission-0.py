# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
- we need to process level by level: points me towards a bfs traversal 

- since we're going to process these nodes level by level: 
    - we use a double ended queue 
    - append from behind and then pop from the left 

establish some base case here: 
    - what should we do if root is none -> then just return [] ? 

'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None: 
            return [] 

        result = [] 
        queue = collections.deque() 
        queue.append(root)
        while queue: 
            q_len = len(queue)
            level = [] 

            for i in range(q_len): 
                node = queue.popleft() 
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)

            result.append(level)

        return result






        