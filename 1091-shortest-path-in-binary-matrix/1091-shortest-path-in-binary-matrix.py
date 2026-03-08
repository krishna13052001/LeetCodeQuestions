from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0] or grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        distance = [[float("inf")] * len(grid) for _ in range(len(grid))]
        queue = deque([(1, (0,0))])
        distance[0][0] = 1
        while queue:
            cost, point = queue.popleft()
            x, y = point
            if distance[x][y] < cost:
                continue
            directions = [(-1,0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]
            for dr, dc in directions:
                nr = x + dr
                nc = y + dc
                new_distance = 1 + cost
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and distance[nr][nc] > new_distance:
                    distance[nr][nc] = new_distance
                    queue.append((new_distance, (nr, nc)))
        if distance[-1][-1] == float("inf"):
            return -1
        return distance[-1][-1]
