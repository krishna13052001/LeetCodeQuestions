class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        d1 = {}
        l = s.split()
        if(len(pattern) != len(l)):
            return False
        for i in range(len(l)):
            if l[i] not in d1:
                d1[l[i]] = pattern[i]
            else:
                if(d1[l[i]] != pattern[i]):
                    return False
            if pattern[i] not in d:
                d[pattern[i]] = l[i]
            else:
                if(d[pattern[i]] != l[i]):
                    return False
        return True