class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return
        length = len(s)
        if(length==1 ):
            return s
        res = s[0]
        for i in range(length):
            cur = self.getPalindrome(s,i,i)
            if(len(cur) > len(res)):
                res = cur
            cur = self.getPalindrome(s,i,i+1)
            if(len(cur)>len(res)):
                res = cur
        return res
    def getPalindrome(self,s,begin,end):
        while(begin >= 0 and end<len(s) and s[begin] == s[end]):
            begin -= 1
            end += 1
        return s[begin+1:end]