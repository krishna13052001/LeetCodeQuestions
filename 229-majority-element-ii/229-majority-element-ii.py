class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        if len(nums) == 2 and nums[0] != nums[1]:
            return nums
        n = len(nums)
        s = n//3
        h = {}
        res = set()
        
        for i in nums:
            if i in h:
                h[i] += 1
                if h[i] > s and i not in res:
                    res.add(i)
            else:
                h[i] = 1
        return list(res)