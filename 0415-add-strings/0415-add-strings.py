class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        res = ""
        overflow = 0
        while i >= 0 and j >= 0:
            sum = int(num1[i]) + int(num2[j]) + overflow
            unit = sum % 10
            overflow = sum // 10
            res += str(unit)
            i -= 1
            j -= 1
        while i >= 0:
            sum = overflow + int(num1[i])
            unit = sum % 10
            overflow = sum // 10
            res += str(unit)
            i -= 1
        while j >= 0:
            sum = overflow + int(num2[j])
            unit = sum % 10
            overflow = sum // 10
            res += str(unit)
            j -= 1
        if overflow != 0:
            res += str(overflow)
        return res[::-1]