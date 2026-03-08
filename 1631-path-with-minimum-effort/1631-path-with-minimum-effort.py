import heapq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        effort = [[float("inf")] * cols for _ in range(rows)]
        effort[0][0] = 0

        heap = [(0, 0, 0)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while heap:
            cur_eff, r, c = heapq.heappop(heap)
            if (r, c) == (rows - 1, cols - 1):
                return cur_eff

            if cur_eff > effort[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    step = abs(heights[r][c] - heights[nr][nc])
                    new_eff = max(cur_eff, step)
                    if new_eff < effort[nr][nc]:
                        effort[nr][nc] = new_eff
                        heapq.heappush(heap, (new_eff, nr, nc))

        return 0
