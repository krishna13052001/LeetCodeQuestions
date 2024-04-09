class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        for idx in range(len(tickets)):
            if idx <= k:
                count += min(tickets[idx], tickets[k])
            else:
                count += min(tickets[idx], tickets[k]-1)
        return count