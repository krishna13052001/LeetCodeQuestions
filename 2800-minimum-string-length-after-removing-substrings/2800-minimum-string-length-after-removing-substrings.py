class Solution:
    def minLength(self, s: str) -> int:
        writer = 0
        reader = 0
        s = list(s)
        while reader < len(s):
            s[writer] = s[reader]
            if writer > 0 and (s[writer] == 'B' or s[writer] == 'D') and s[writer] == chr(ord(s[writer - 1]) + 1):
                writer -= 1
            else:
                writer += 1
            reader += 1
        return writer