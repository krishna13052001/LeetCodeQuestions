class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = maxlen = maxf = 0
        d = {}
        while r < len(s):
            if d.get(s[r],-1) ==-1:
                d[s[r]] = 1
                
            else:
                d[s[r]] += 1
            maxf = max(maxf,d[s[r]])
            if ((r - l + 1) - maxf > k):
                d[s[l]] -= 1
                maxf = 0
                for key, value in d.items():
                    print(key, value)
                    maxf = max(maxf,value)
                l += 1
            if ((r-l+1)-maxf <= k):
                
                maxlen = max(maxlen, r-l+1 )
            r += 1
        return maxlen
            