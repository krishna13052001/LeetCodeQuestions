class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res= []
        n = len(land)
        if n  == 0:
            return res
        m = len(land[0])
        for i in range(n):
            for j in range(m):
                if land[i][j] == 1:
                    innerIIdx = i
                    innerJIdx = j
                    while innerIIdx < n and land[innerIIdx][j] == 1:
                        innerJIdx = j
                        while innerJIdx < m and land[innerIIdx][innerJIdx] == 1:
                            land[innerIIdx][innerJIdx] = 0
                            innerJIdx += 1
                        innerIIdx += 1
                    res.append([i,j, innerIIdx-1, innerJIdx-1])
        return res