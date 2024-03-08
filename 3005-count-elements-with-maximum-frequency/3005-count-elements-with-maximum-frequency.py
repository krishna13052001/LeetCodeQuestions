class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        req = {}
        maxValue = float('-inf')
        for i in nums:
            if req.get(i, -1) != -1:
                req[i] += 1
            else:
                req[i] = 1
            maxValue = max(maxValue, req[i])
        count = 0
        for key, values in req.items():
            if values == maxValue:
                count += 1
        return count * maxValue