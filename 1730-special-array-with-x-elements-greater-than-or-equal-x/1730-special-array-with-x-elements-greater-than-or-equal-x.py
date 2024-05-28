class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        for i in range(n+1):
            c=i
            for j in nums:
                if j>=i:
                    c-=1
                if c<0:
                    break
            if c==0:
                return i
        return -1
