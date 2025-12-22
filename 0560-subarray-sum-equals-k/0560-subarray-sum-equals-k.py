class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        count = 0
        res = 0
        for idx, num in enumerate(nums):
            count += num
            if count - k in d:
                res += d[count-k]
            d[count] = d.get(count, 0) + 1
        return res