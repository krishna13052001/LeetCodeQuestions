class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        d1 = {}
        lengthS = len(s)
        lengthT = len(t)
        if(lengthS != lengthT):
            return False
        for i in range(lengthS):
            if t[i] not in d1:
                d1[t[i]] = s[i]
            else:
                if(d1[t[i]] != s[i]):
                    return False
            if s[i] not in d:
                d[s[i]] = t[i]
            else:
                if(d[s[i]] != t[i]):
                    return False
        return True