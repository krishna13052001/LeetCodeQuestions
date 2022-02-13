class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        for num in nums:
            result += [i +[num] for i in result if i + [num] not in result]
        return result