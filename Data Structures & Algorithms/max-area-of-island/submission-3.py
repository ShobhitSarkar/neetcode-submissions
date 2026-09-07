"""
-- high level algorithm: 
    - "seeing till where the islands extends out till" = bfs problem 
        - in this we're basically going to sink the islands 
        - also calculate the area (every time that we sink an island, one unit increases)
        - coming out of the recursive call - update the max_area variable or something 
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_rows = len(grid)
        max_cols = len(grid[0])

        def check(row, col): 
            """
            helper method to enforce constraints 
            """

            if row < 0 or col < 0 or row >= max_rows or col >= max_cols or grid[row][col] == 0: 
                return False 
            
            return True 
        
        def bfs(row, col): 
            """
            bfs traversal to find out till "where" the island extends out till 
            """
            self.current_area = 0 

            if check(row, col) == False: 
                return False 

            grid[row][col] = 0 
            self.current_area += 1 

            self.current_area += bfs(row + 1, col)
            self.current_area += bfs(row - 1, col)
            self.current_area += bfs(row, col + 1)
            self.current_area += bfs(row, col - 1)

            return self.current_area

        max_area = float('-inf')

        for i in range(len(grid)): 
            for j in range(len(grid[i])): 
                if grid[i][j] == 1: 
                    area = bfs(i, j)
                    max_area = max(area, max_area)


        return max_area if max_area != float('-inf') else 0 

        

