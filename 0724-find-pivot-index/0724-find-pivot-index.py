class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        idx = left = 0
        while idx < len(nums):
            if left == (total - left - nums[idx]):
                return idx
            left += nums[idx]
            idx += 1
        return -1