"""
-- given information: 
    - 1 = land 
    - 0 = water 

-- high level algorithm: 
    - init a couple of variables: 
        - num_islands = keeping track of the number of islands that are available 
    - starting the find for the first island: 
        - loop through the grid, start when you encounter the first 1 (land)
    - just having one island "node" doesn't mean that's it: we've gotta see till where it stretches: bfs
        - that entire island is going to increase the count by 1 
    - if we just sink the island, then we won't have to count it again 
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        max_rows = len(grid)
        max_cols = len(grid[0])

        def check(row, col): 
            """
            helper method to enforce constraints
            """

            if row < 0 or col < 0 or row >= max_rows or col >= max_cols or grid[row][col] == "0": 
                return False 
            
            return True
        
        def bfs(row, col): 
            """
            helper method to see where the island extends out to 
            """

            if check(row, col) == False: 
                return False 

            grid[row][col] = "0" 

            bfs(row + 1, col)
            bfs(row - 1, col)
            bfs(row, col + 1)
            bfs(row, col -1)

        ## finding the islands 

        num_islands = 0 

        for i in range(len(grid)): 
            for j in range(len(grid[i])): 
                if grid[i][j] == "1": 
                    num_islands += 1 
                    bfs(i, j)
        
        return num_islands

            




        