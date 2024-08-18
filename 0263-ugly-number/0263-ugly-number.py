class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        for num in [5, 3, 2]:
            while n % num == 0:
                n //= num
        return n == 1