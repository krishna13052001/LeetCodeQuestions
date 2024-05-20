count = 0
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subset = [None]*(len(nums))
        def helper(nums, subset,i, XorValue):
            if( i== len(nums)):
                global count
                count += XorValue
            else:
                subset[i] = None
                helper(nums,subset,i+1,XorValue)
                subset[i] = nums[i]
                XorValue ^= nums[i]
                helper(nums,subset,i+1,XorValue)
        helper(nums,subset,0,0)
        global count
        previous_count = count
        count = 0
        return previous_count