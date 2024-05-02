class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for idx, number in enumerate(nums):
            if idx > 0 and number == nums[idx-1]:
                continue
            left, right = idx +1, len(nums) -1
            while left < right:
                
                count = number + nums[left] + nums[right]
                if count == 0:
                    res.append([number, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                elif count < 0:
                    left += 1
                else:
                    right -= 1
        return res