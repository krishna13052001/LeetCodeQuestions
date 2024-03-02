class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        left = 0
        right = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            val = -1
            if( abs(nums[left]) < abs(nums[right])):
                val = nums[right]
                right -= 1
            else:
                val = nums[left]
                left += 1
            res[i] = val * val
        return res