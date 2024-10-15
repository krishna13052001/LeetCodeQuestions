class Solution:
    def smallestString(self, s: str) -> str:
        def onego(s):
            return "".join(chr(ord(x)-1) for x in s)

        if s == 'a':
            return 'z'
        elif 'a' not in s:
            return onego(s)
        elif s.count('a') == 1:
            if s[0] == 'a':
                return 'a'+onego(s[1:])
            else:
                return onego(s[:s.index('a')])+s[s.index('a'):]
        else:
            if s[0] != 'a':
                return onego(s[:s.index('a')])+s[s.index('a'):]

            elif len(s) == s.count('a'):
                return s[:-1]+'z'
            else:
                idx = 0
                for i in range(len(s)):
                    if s[i] == 'a':
                        continue
                    else:
                        idx = i
                        break
                if 'a' not in s[idx:]:
                    return s[:idx]+onego(s[idx:])
                else:
                    ss = s[idx:]
                    ii = idx + ss.index('a')
                    return s[:idx]+onego(s[idx:ii])+s[ii:]
        