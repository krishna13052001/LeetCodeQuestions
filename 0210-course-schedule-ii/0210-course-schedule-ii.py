from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegre = [0] * numCourses
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
            indegre[edge[0]] += 1
        
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
        if len(toposort) == numCourses:
            return toposort
        return []