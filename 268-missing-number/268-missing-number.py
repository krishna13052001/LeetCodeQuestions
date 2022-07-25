class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_n = None
        n = len(nums)

        i = 0
        while i < n:
            if nums[i] == n:
                num_n = nums[i]
                nums[i] = None
                i += 1
            elif nums[i] is not None and nums[i] != i:
                j = nums[i]
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        if not num_n:
            return n
        return nums.index(None)
