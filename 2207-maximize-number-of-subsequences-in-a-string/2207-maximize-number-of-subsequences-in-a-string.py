class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        res, first, second = 0, 0, 0
        for c in text:
            if c == pattern[1]:
                second += 1
                res += first
            if c == pattern[0]:
                first += 1
        return res + max(first, second)
