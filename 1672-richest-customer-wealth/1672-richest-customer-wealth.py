class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for wealth in accounts:
            res =max(sum(wealth),res)
        return res