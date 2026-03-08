from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for values in prerequisites:
            indegree[values[1]] += 1
            adj[values[0]].append(values[1])
        
        queue = deque()
        for idx in range(numCourses):
            if indegree[idx] == 0:
                queue.append(idx)
        
        toposort = []
        while queue:
            node = queue.popleft()
            toposort.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return len(toposort) == numCourses