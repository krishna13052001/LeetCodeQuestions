class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if len(nums) == 0:
            return res 
        value  = float('-inf')
        preValue = float('-inf')
        n = len(nums)
        for i in range(n):
            if value == float('-inf'):
                value = nums[i]
                preValue = nums[i]
            elif value + 1 == nums[i]:
                value += 1
            else:
                if value == preValue:
                    res.append('{}'.format(value))
                else:
                    res.append('{}->{}'.format(preValue, value))
                value = nums[i]
                preValue = nums[i]
        if value == preValue:
            res.append('{}'.format(value))
        else:
            res.append('{}->{}'.format(preValue, value))
        return res