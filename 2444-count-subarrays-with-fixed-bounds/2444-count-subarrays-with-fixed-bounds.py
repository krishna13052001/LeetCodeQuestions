class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        non_range_index = min_index = max_index = -1
        length = len(nums)
        ans = 0
        for i in range(length):
            if nums[i] < minK or nums[i] > maxK:
                non_range_index = i
            if nums[i] == minK:
                min_index = i
            if nums[i] == maxK:
                max_index = i
            ans += max(0, min(min_index, max_index) - non_range_index)
            print(ans,min_index, max_index)
        return ans