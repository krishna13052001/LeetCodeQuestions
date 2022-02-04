class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        res = 0
        count = 0
        for i in range(len(nums)):
            if(nums[i] == 1):
                count += 1
            else:
                count -= 1
            if(count == 0):
                res = max(res,i+1)
            elif count not in d:
                d[count] = i
            else:
                res = max(res,i - d[count])
        return res