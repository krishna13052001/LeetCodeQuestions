class Solution:
    dp = {}
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        left, right = 0 ,0
        if self.dp.get(n-1,-1) != -1:
            left = self.dp[n-1]
        else:
            left = self.climbStairs(n-1)
            self.dp[n-1] = left
        if self.dp.get(n-2,-1) != -1:
            right = self.dp[n-2]
        else:
            right = self.climbStairs(n-2)
            self.dp[n-1] = right
        return left + right
        