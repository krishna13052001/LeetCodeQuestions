class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1, prev2 = 0, 0

        for i in range(len(cost)):
            current = cost[i] + min(prev1, prev2)
            prev2, prev1 = prev1, current
        return min(prev1, prev2)
