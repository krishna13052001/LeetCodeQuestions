class Solution:
    dp = [-1]*46
    dp[0]=1
    dp[1]=1
    def findAns(self,n):
        if(self.dp[n]!=-1):
            return self.dp[n]
        elif(n<0):
            return 0
        else:
            self.dp[n] = self.findAns(n-1) + self.findAns(n-2)
            return self.dp[n]
    def climbStairs(self, n: int) -> int:
        return self.findAns(n)