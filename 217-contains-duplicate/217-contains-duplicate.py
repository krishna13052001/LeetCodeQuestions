class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if i not in d:
                d[i]=0
            else:
                return True
        return False
        