class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def helper(n, quantities, max_limit):
            try:
                no_of_stores_required =0
                for quantity in quantities:
                    no_of_stores_required += math.ceil(quantity/max_limit)
                return no_of_stores_required <= n
            except:
                return False
        
        max_quanity = max(quantities)
        length = len(quantities)
        left = 0
        right = max_quanity
        ans = length
        while left <= right:
            mid = (left + right)//2
            if helper(n, quantities, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
