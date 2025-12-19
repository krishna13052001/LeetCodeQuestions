class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
        for char in t:
            occ = d.get(char, -1)
            if occ == -1:
                return False
            elif occ > 1:
                d[char] -= 1
            elif occ == 1:
                del d[char]
        return True

