from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        
        def bfs(r: int, c: int):
            queue = deque([(r, c)])
            visited[r][c] = True
            dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            while queue:
                row, col = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows and 0 <= nc < cols and 
                        not visited[nr][nc] and grid[nr][nc] == "1"):
                        visited[nr][nc] = True
                        queue.append((nr, nc))
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and grid[r][c] == "1":
                    count += 1
                    bfs(r, c)
        return count
