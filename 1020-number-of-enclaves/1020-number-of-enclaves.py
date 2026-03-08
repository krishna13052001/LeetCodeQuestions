from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        queue = deque([])
        for rdx in range(rows):
            if grid[rdx][0] == 1:
                queue.append((rdx, 0))
                visited[rdx][0] = True
            if grid[rdx][cols - 1] == 1:
                queue.append((rdx, cols -1))
                visited[rdx][cols - 1] = True
        
        for cdx in range(cols):
            if grid[0][cdx] == 1:
                queue.append((0, cdx))
                visited[0][cdx] = True
            if grid[rows - 1][cdx] == 1:
                queue.append((rows - 1, cdx))
                visited[rows - 1][cdx] = True
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr = dr + row
                nc = dc + col
                if (0 <= nr < rows and 0 <= nc < cols 
                and grid[nr][nc] == 1 and not visited[nr][nc]):
                    visited[nr][nc] = True
                    queue.append((nr, nc))
        count = 0
        for rdx in range(rows):
            for cdx in range(cols):
                if grid[rdx][cdx] == 1 and not visited[rdx][cdx]:
                    count += 1
        return count