class Solution:
    def pivotInteger(self, n: int) -> int:
        left, right = 0, n
        leftSum, rightSum = left, right
        if n == 1:
            return n
        while left < right:
            if leftSum < rightSum:
                left += 1
                leftSum += left
            else:
                right -= 1
                rightSum += right
            if leftSum == rightSum and left + 1 == right -1 :
                return left + 1
        return -1
            