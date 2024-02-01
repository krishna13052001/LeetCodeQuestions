class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        res= []
        for i in range(2, len(nums), 3):
            if nums[i] - nums[i-2] <= k:
               res.append([nums[i], nums[i-1], nums[i-2]])
            else:
                return []
        return res
        