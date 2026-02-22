class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = value = sum(nums[:k])
        for idx in range(k, len(nums)):
            value = value - nums[idx-k] + nums[idx]
            result = max(result, value)
        return result/ k