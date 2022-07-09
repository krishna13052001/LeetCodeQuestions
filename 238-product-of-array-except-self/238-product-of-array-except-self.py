class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0]*length
        res[0] = nums[0]
        for i in range(1,length):
            res[i] = res[i-1] * nums[i]
        product = nums[length - 1]
        res[length-1] = res[length-2]
        for i in range(length-2,0,-1):
            res[i] = res[i-1] * product
            product *= nums[i] 
        res[0] = product
        return res