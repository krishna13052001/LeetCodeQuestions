from collections import deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))

        dist = [float("inf")] * n
        dist[src] = 0
        queue = deque()
        queue.append((0, src, 0))
        while queue:
            stops, node, cost = queue.popleft()
            if stops > k:
                continue

            for adj, w in graph[node]:
                new_cost = cost + w
                if new_cost < dist[adj] and stops <= k:
                    dist[adj] = new_cost
                    queue.append((stops + 1, adj, new_cost))

        return -1 if dist[dst] == float("inf") else dist[dst]
