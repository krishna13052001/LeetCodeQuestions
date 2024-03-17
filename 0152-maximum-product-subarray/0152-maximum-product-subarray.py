class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float("-inf")
        prefix, sufix = 1, 1
        for i in range(len(nums)):
            if prefix == 0:
                prefix = 1
            if sufix == 0:
                sufix = 1
            prefix *= nums[i]
            sufix *= nums[len(nums) - i - 1]
            ans = max(ans, prefix, sufix)
        return ans