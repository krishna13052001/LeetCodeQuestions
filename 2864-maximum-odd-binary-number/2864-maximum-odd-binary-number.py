class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0
        for i in s:
            if i == "1":
                count += 1
        length = len(s)
        return "1" * (count -1) + "0" * (length - count) + "1"