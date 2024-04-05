class Solution:
    def makeGood(self, s: str) -> str:
        alpha = []
        idx = 0
        while idx < len(s):
            if alpha and alpha[-1] != s[idx] and alpha[-1].lower() == s[idx].lower():
                alpha.pop()
            else:
                alpha.append(s[idx])
            idx += 1
        return "".join(alpha)