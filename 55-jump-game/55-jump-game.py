class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        reachable = 0
        for i in range(length):
            if (reachable < i):
                return False
            reachable = max(reachable,i+nums[i])
        return True