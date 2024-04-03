class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        res= []
        for i in range(1 << length):
            s = []
            for j in range(length):
                if i & (1 << j):
                    s.append(nums[j])
            res.append(s)
        return res