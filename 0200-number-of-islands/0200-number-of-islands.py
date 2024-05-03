

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
        n = len(grid)
        m = len(grid[0])
        mat = grid
        count_1 = 0
        count = 0
        i,j = 0,0
        while(i < n and j < m):
            if(mat[i][j] == '1'):
                count += 1
                self.find(mat,i,j)
            j += 1
            if(j >= m):
                i += 1
                j = 0
        return count      