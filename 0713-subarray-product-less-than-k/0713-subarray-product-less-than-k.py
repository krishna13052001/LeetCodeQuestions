class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = right = 0
        product = 1
        res = 0
        length = len(nums)
        for right in range(length):
            product *= nums[right]
            if product >= k:
                while product >= k and left <= right:
                    product /= nums[left]
                    left += 1
            res += (right -left + 1)
        return res
            