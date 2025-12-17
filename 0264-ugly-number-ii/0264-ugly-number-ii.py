class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1] * n
        i2, i3, i5 = 0, 0, 0

        for i in range(1, n):
            next2, next3, next5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            value = min(next2, next3, next5)
            ugly[i] = value
            if value == next2:
                i2 += 1
            if value == next3:
                i3 += 1
            if value == next5:
                i5 += 1
        return ugly[-1]