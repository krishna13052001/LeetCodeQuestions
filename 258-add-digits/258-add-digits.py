class Solution:
    def addDigits(self, num: int) -> int:
        digit =num%9
        if digit == 0 and num != 0:
            return 9
        else:
            return digit