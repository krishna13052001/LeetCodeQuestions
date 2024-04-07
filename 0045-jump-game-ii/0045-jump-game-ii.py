class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums)-1
        idx = goal - 1
        count = 0

        while goal > 0:
            for i in range(goal-1,-1,-1):
                if i+nums[i] >= goal:
                    idx = min(idx,i)
            goal = idx
            count += 1
        return count