class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        count_for_zeros = 0
        count_for_ones = 0
        result = 0
        for idx, num in enumerate(nums):
            if num == 1:
                count_for_ones += 1
            else:
                count_for_zeros += 1
            diff = count_for_ones - count_for_zeros
            if diff not in d:
                d[diff] = idx
            if diff == 0:
                result = max(result, 2 * count_for_ones)
            elif diff in d:
                result = max(result, idx - d[diff])
        print(d)
        return result
                