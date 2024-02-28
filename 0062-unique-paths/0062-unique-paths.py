class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * m for _ in range(n)]
        print(dp)
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    up,down = 0,0
                    if i > 0:
                        up = dp[i-1][j]
                    if j > 0:
                        down = dp[i][j-1]
                    dp[i][j] = up+down
        print(dp,m,n)
        return dp[n-1][m-1]