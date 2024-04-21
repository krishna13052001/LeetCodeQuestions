class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        visited = [False] * n
        d = {}
        for i in edges:
            if i[0] not in d:
                d[i[0]] = [i[1]]
            else:
                d[i[0]].append(i[1])
            if i[1] not in d:
                d[i[1]]  = [i[0]]
            else:
                d[i[1]].append(i[0])
        # queue = [start]
        # visited[start] = True
        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            for child in d.get(node, []):
                if not visited[child]:
                    dfs(child)
                    
        dfs(start)
        return visited[end]
            
            