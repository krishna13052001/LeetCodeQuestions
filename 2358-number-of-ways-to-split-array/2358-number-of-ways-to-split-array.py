class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum  = sum(nums)
        prefix_sum = 0
        count = 0
        idx = 0
        while idx < len(nums) - 1:
            prefix_sum += nums[idx]
            count+=(2*prefix_sum>=total_sum)
            idx += 1
        return count