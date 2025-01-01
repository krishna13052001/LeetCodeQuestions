class Solution:
    def maxScore(self, s: str) -> int:
        right_1s = 0
        left_0s = 0
        res = 0
        for i in s:
            if i == "1":
                right_1s += 1
        
        if s[0] == "0":
            left_0s += 1
        else:
            right_1s -= 1
        pos = 1
        res = left_0s + right_1s
        while pos < len(s)-1:
            if s[pos] == "0":
                left_0s += 1
            else:
                right_1s -= 1
            res = max(res, left_0s + right_1s)
            pos += 1
        return res

