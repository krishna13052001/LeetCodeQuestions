class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[-1] * (len(obstacleGrid[0])) for _ in range(len(obstacleGrid))]
        print(dp, m,n)
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] ==1:
                    dp[i][j] = 0
                elif i ==0 and j ==0:
                    dp[i][j] = 1
                elif i < 0 or j < 0:
                    dp[i][j] = 0
                else:
                    up,down =0,0
                    if i > 0:
                        up = dp[i-1][j]
                    if j > 0:
                        down = dp[i][j-1]
                    dp[i][j] = up + down
        return dp[len(obstacleGrid)-1][len(obstacleGrid[0])-1]