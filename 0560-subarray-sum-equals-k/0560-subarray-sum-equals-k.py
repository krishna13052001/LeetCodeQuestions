class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        has_map = defaultdict(int)
        has_map[0] = 1
        pre_sum, res = 0, 0
        for num in nums:
            pre_sum += num
            res += (has_map[pre_sum-k])
            has_map[pre_sum] += 1
        return res