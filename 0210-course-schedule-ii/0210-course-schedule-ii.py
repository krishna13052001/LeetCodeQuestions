from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegre = [0] * numCourses
        for edge in prerequisites:
            graph[edge[0]].append(edge[1])
            indegre[edge[1]] += 1
        
        queue = deque()
        for idx in range(numCourses):
            if indegre[idx] == 0:
                queue.append(idx)

        toposort = []
        while queue:
            node = queue.popleft()
            toposort.append(node)
            for neighbor in graph[node]:
                indegre[neighbor] -= 1
                if indegre[neighbor] == 0:
                    queue.append(neighbor)
        for idx in range(numCourses):
            if indegre[idx] != 0:
                return []
        return toposort[::-1]