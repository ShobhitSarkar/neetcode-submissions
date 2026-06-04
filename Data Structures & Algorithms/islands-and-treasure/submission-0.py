"""
we need to identify all of the "treasure chests" and then
the minimum distance between the nodes is going to be between them

"""

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        max_rows = len(grid)
        max_cols = len(grid[0])


        queue = collections.deque() 
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        for i in range(len(grid)): 
            for j in range(len(grid[i])): 
                if grid[i][j] == 0: 
                    queue.append((i, j))

        def check (row, col): 
            if row < 0 or col < 0 or row >= max_rows or col >= max_cols or grid[row][col] == -1: 
                return False 

            return True 
        
        while queue: 

            row, col = queue.popleft() 

            for dr, dc in directions: 
                nr, nc = dr + row, dc + col

                if not check(nr, nc): 
                    continue
                
                if grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[row][col] + 1 
                    queue.append((nr, nc))


                

        