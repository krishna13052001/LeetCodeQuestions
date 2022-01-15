class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if(len(arr)==1):
            return 0
        d = {}
        n = len(arr)
        for i in range(n):
            if arr[i] not in d:
                d[arr[i]] = [i]
            else:
                d[arr[i]].append(i)
        visited = set([])
        q = [0]
        visited.add(0)
        count = 0
        while(len(q)!=0):
            length  = len(q)
            while(length>0):
                length -= 1
                v = q.pop(0)
                if(v == n-1):
                    return count
                adjList = d[arr[v]]
                adjList.append(v+1)
                adjList.append(v-1)
                for j in adjList:
                    if(j>=0 and j<n and j not in visited):
                        q.append(j)
                        visited.add(j)
                d[arr[v]] = []
            count += 1
        return -1
        