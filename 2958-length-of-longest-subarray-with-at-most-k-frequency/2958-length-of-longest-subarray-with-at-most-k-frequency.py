class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d = {}
        ans = i = j = 0
        length = len(nums)
        while j < length:
            if d.get(nums[j],-1) == -1:
                d[nums[j]] = 1
            else:
                d[nums[j]] += 1
            while i <= j and d[nums[j]] > k:
                d[nums[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
            j += 1
        return ans