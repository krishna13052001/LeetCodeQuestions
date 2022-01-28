class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            nums[abs(num)-1] = abs(nums[abs(num)-1])*-1
        res = []
        for i in range(len(nums)):
            if(nums[i] >=0):
                res.append(i+1)
        return res