class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        total_sum = 0
        count = 0

        for i in range(1, n + 1):
            if i in banned:
                continue
            total_sum += i
            if total_sum > maxSum:
                break
            count += 1

        return count