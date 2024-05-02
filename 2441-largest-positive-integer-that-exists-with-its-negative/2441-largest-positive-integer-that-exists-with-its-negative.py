class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        d = {}
        maxi = -1
        for num in nums:
            if num < 0:
                if d.get(abs(num),-1) != -1:
                    maxi = max(maxi, abs(num))
                else:
                    d[num] = 1
            else:
                if d.get(num *-1, -1) != -1:
                    maxi = max(maxi, num)
                else:
                    d[num] = 1
        return maxi
                    