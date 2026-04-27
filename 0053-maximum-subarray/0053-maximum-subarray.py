class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = count = nums[0]
        for idx in range(1, len(nums)):
            if count < 0:
                count = 0
            count += nums[idx]
            result = max(result, count)
        return result