class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, num in enumerate(nums):
            other_element = target - num
            if other_element in d:
                return [d[other_element], idx]
            else:
                d[num] = idx
        return 