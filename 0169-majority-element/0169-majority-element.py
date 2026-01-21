class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        possible = length // 2
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
            if d[num] > possible:
                return num
        