class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low,high=1,100000
        while(low<=high):
            mid = low + (high-low)//2
            target = mid*mid
            if(target == num):
                return True
            elif(target>num):
                high = mid-1
            else:
                low =mid+1
        return False