class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for idx in range(n):
            if nums[idx] < 0:
                nums[idx] = 0
        for idx in range(n):
            val = abs(nums[idx])
            if 1 <= val <= n:
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
        print( nums)
        for i in range(n):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1