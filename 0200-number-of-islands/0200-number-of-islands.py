

class Solution:
    def find(self,mat,i,j):
        if(i< 0 or j<0):
            return
        try:
            if(mat[i][j] == '1'):
                mat[i][j] = '0'
                # print(i,j,mat[i][j])
                self.find(mat,i,j+1)
                self.find(mat,i,j-1)
                self.find(mat,i+1,j)
                self.find(mat,i-1,j)
        except:
            pass

    def numIslands(self, grid: List[List[str]]) -> int:
        # n = int(input())
        # mat = []
        n = len(grid)
        m = len(grid[0])
        mat = grid
        count_1 = 0
        # for i in range(n):
        #     arr = list(map(int,input().split()))
        #     mat.append(arr)
        # print(mat)
        count = 0
        i,j = 0,0
        while(i < n and j < m):
            if(mat[i][j] == '1'):
                # print("Hi")
                # print(i,i,mat[i][j])
                count += 1
                self.find(mat,i,j)
            j += 1
            # print("Jvalue ",j,m)
            if(j >= m):
                i += 1
                j = 0
        return count      