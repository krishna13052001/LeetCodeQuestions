class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefix_sum = [0] * (n + 1)
        for i, customer in enumerate(customers):
            prefix_sum[i + 1] = prefix_sum[i] + (1 if customer == 'Y' else 0)
        
        totalY = prefix_sum[n]
        best_hour = 0
        min_penalty = float('inf')

        for j in range(n + 1):
            open_penalty = j - prefix_sum[j]
            closed_penalty = totalY - prefix_sum[j]
            penalty = open_penalty + closed_penalty
            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = j

        return best_hour