from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        length = len(isConnected)
        visited = [False] * length
        def bfs(node):
            queue = deque([node])
            visited[node] = True
            while queue:
                node = queue.popleft()
                for neighbor, val in enumerate(isConnected[node]):
                    if neighbor != node and val == 1 and not visited[neighbor]:
                        queue.append(neighbor)
                        visited[neighbor] = True
        count = 0
        for i in range(length):
            if not visited[i]:
                count += 1
                bfs(i)
                print(visited)
        return count