class Solution:
    dp=[-1]*38
    dp[0]=0
    dp[1]=1
    dp[2]=1
    def findNTri(self,n):
        if(n<0):
            return 0
        if(self.dp[n]!=-1):
            return self.dp[n]
        else:
            self.dp[n] = self.findNTri(n-1)+self.findNTri(n-2)+self.findNTri(n-3)
            return self.dp[n]
    def tribonacci(self, n: int) -> int:
        return self.findNTri(n)