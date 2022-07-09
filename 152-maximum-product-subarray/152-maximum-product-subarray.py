class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = mins = prod = nums[0]
        for i in range(1,len(nums)):
            if(nums[i]<0):
                maxi,mins = mins,maxi
            maxi = max(nums[i],maxi*nums[i])
            mins = min(nums[i],mins*nums[i])
            prod = max(prod,maxi)
        return prod