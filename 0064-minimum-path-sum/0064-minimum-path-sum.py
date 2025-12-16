class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows == 0:
            return 0
        
        cols = len(grid[0])
        if cols == 0:
            return 0
        
        result = [[0] * cols for _ in range(rows)]
        result[0][0] = grid[0][0]
        for i in range(1, cols):
            result[0][i] = result[0][i-1] + grid[0][i]
        
        for j in range(1, rows):
            result[j][0] = result[j-1][0] + grid[j][0]
        
        for i in range(1, rows):
            for j in range(1, cols):
                result[i][j] = grid[i][j] + min(result[i-1][j], result[i][j-1])
        return result[rows-1][cols-1]