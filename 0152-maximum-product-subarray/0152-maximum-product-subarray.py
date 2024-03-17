class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float("-inf")
        prefix, sufix = 1, 1
        n = len(nums)
        for i in range(n):
            if prefix == 0:
                prefix = 1
            if sufix == 0:
                sufix = 1
            prefix *= nums[i]
            sufix *= nums[n - i - 1]
            ans = max(ans, prefix, sufix)
        return ans