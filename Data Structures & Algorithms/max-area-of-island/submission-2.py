"""
identifying an island: 
    - start: when we encounter 1
    - end: when it's surrounded by water 

- start with any position in the matrix
- once you encounter an island, grow it
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_rows = len(grid)
        max_cols = len(grid[0])


        def check(row, col): 
            """
            enforce constraints 
            """
            if row < 0 or col < 0 or row >= max_rows or col >= max_cols or grid[row][col] == 0: 
                return False 
            return True 
        
        def bfs(row, col): 
            """
            grow the islands 
            """

            if check(row, col) == False: 
                return 0
        
            self.area = 1
            grid[row][col] = 0

            self.area += bfs(row + 1, col)
            self.area += bfs(row - 1, col)
            self.area += bfs(row, col + 1)
            self.area += bfs(row, col - 1)

            return self.area
        
        max_area = float('-inf')

        for i in range(len(grid)): 
            for j in range(len(grid[i])): 
                if grid[i][j] == 1: 
                    area = bfs(i , j)
                    max_area = max(max_area, area)


        return max_area if max_area != float('-inf') else 0
                    