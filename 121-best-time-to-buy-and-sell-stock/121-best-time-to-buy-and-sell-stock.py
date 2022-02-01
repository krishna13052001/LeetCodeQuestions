import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_value = sys.maxsize
        for price in prices:
            min_value = min(min_value, price)
            if(profit < price - min_value ):
                profit = price-min_value
        return profit
            