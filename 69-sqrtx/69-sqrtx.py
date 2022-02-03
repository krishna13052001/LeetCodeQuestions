import sys
class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        ans = 0
        end = 1000020394
        while(low<=end):
            mid = low+(end-low)//2
            # print(mid,end)
            if(mid*mid<=x):
                ans = mid
                low = mid+1
            else:
                end = mid -1
        return ans
            