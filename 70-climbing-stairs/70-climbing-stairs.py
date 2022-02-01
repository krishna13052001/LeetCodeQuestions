class Solution:
    """dp = [-1]*46
    dp[0]=1
    dp[1]=1
    def findAns(self,n):
        if(self.dp[n]!=-1):
            return self.dp[n]
        elif(n<0):
            return 0
        else:
            self.dp[n] = self.findAns(n-1) + self.findAns(n-2)
            return self.dp[n]"""
    
    def climbStairs(self, n: int) -> int:
        # return self.findAns(n)
        prev2,prev1 = 1,1
        for i in range(2,n+1):
            curr = prev1+prev2
            prev2 = prev1
            prev1=curr
        return prev1