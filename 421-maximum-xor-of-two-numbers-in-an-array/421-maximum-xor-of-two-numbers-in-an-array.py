class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ret = 0
        for i in range(31,-1,-1):
            prefixes = set(num >> i for num in nums)
            ret <<= 1
            cur = ret + 1
            for p in prefixes:
                if cur ^ p in prefixes:
                    ret = cur
                    break
        return ret