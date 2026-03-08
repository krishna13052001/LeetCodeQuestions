from typing import List
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return mat
        rows = len(mat)
        cols = len(mat[0])
        visited = [[False] * cols for _ in range(rows)]
        res = [[0] * cols for _ in range(rows)]
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row, col, 0))
                    visited[row][col] = True
        while queue:
            row, col, distance = queue.popleft()
            res[row][col] = distance
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nrow = row + dr
                ncol = col + dc
                if 0 <= nrow < rows and 0 <= ncol < cols and not visited[nrow][ncol]:
                    visited[nrow][ncol] = True
                    # res[nrow][ncol] = distance + 1
                    queue.append((nrow, ncol, distance + 1))
        return res
