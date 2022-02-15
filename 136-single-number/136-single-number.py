class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        length = len(nums)
        for i in range(1,length):
            res ^=nums[i]
        return res