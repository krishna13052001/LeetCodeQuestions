class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_zero_index = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                first_zero_index = i
                break
        if first_zero_index == -1:
            return
        index = first_zero_index + 1
        while index < len(nums):
            if nums[index] != 0:
                nums[index], nums[first_zero_index] = nums[first_zero_index], nums[index]
                first_zero_index +=1
                index += 1
            else:
                index += 1

        