class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if len(piles) > H:
            return None

        n = len(piles)
        hi = max(piles) + 1
        lo = 1
        while lo < hi:
            mid = (lo + hi) // 2
            if sum( math.ceil(piles[i] / mid) for i in range(n)) > H:
                lo = mid + 1
            else:
                hi = mid

        return lo