class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        l = []
        for i in s:
            if i == "(":
                l.append(i)
            elif i == ")":
                count = max(count, len(l))
                l.pop()
        return count