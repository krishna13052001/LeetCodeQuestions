import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pat = re.compile(p)
        sub = pat.match(s)
        if(sub != None and sub.span()[1] == len(s)):
            return True
        return  False