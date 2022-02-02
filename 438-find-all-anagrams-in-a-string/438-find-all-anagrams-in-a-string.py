class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        a = [0]*26
        b = [0]*26
        window = len(p)
        length = len(s)
        if(length < window):
            return []
        left,right = 0,0
        while(right<window):
            a[ord(s[right])-ord('a')] += 1
            b[ord(p[right])-ord('a')] += 1
            right += 1
        right -= 1
        while(right<length):
            if(a == b):
                res.append(left)
            right +=1 
            if(right<length):
                a[ord(s[right])-ord('a')] += 1
            a[ord(s[left])-ord('a')] -= 1
            left += 1
        return res
            