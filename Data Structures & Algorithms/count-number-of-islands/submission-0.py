"""
how do we know it's an island: 
    - when we first encounter one 
        - if we come accross a 1 
    - when it ends 
        - when it's surrounded by water, ie 0s 

how do we keep track of counted islands: 
    - we'll just update the islands because we don't want to count them again 
    - we'll "sink" them 


"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        max_rows = len(grid)
        max_cols = len(grid[0])
        
        def check(row, col): 
            """
            enforce constraints 
            """
            
            if row < 0 or col < 0 or row >= max_rows or col >= max_cols or grid[row][col] == "0": 
                return False 

            return True 
        
        
        def bfs(row, col): 
            """
            grow the island, one step at a time 
            """

            if check(row, col) == False: 
                return 

            grid[row][col] = "0"

            bfs(row + 1, col)
            bfs(row -1, col)
            bfs(row, col + 1)
            bfs(row, col - 1)

        
        num_of_islands = 0 

        for i in range(len(grid)): 
            for j in range(len(grid[i])): 
                if grid[i][j] == "1": 
                    num_of_islands += 1 
                    bfs(i, j)

        return num_of_islands 
        

        