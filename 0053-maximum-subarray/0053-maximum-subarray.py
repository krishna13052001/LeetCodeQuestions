class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        count = 0
        for num in nums:
            count += num
            maxi = max(maxi, count)
            if count < 0:
                count = 0
        return maxi