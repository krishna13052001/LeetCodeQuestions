class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1] * len(nums)
        sufix_product = [1] * len(nums)

        for idx in range(1, len(nums)):
            prefix_product[idx] = prefix_product[idx-1] * nums[idx-1]

        sufix_products = 1 
        for idx in range(len(nums)-2, -1, -1):
            sufix_products *= nums[idx+1]
            prefix_product[idx] *= sufix_products
        return prefix_product
