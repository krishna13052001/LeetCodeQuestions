class Solution:
    k = 0
    dp = []
    n = 0
    def solve(self,id, arr):
        if id >= self.n:
            return 0
        if self.dp[id] != -1:
            return self.dp[id]
        maxValue = 0
        ans = 0
        for j in range(id, min(self.n, id+ self.k)):
            maxValue = max(maxValue, arr[j])
            ans = max(ans,(j-id+1) * maxValue + self.solve(j+1,arr))
        self.dp[id] = ans
        return ans
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        self.n = len(arr)
        self.k = k
        self.dp = [-1] * self.n
        return self.solve(0,arr)
        