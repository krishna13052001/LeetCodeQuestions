from sortedcontainers import SortedSet
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [False] * n
        path_visited = [False] * n
        check = [False] * n
        def dfs(index):
            visited[index] = True
            path_visited[index] = True

            for neighbor in graph[index]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif path_visited[neighbor]:
                    return True
            path_visited[index] = False
            check[index] = True
            return False

        for i in range(n):
            if not visited[i]:
                dfs(i)
        res = []
        for i in range(n):
            if check[i] == True:
                res.append(i)
        return res