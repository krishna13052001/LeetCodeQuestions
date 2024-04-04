class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        open_count = 0
        l = []
        for i in s:
            if i == "(":
                open_count += 1
            elif i == ")":
                open_count -= 1
            count = max(count, open_count)
        return count