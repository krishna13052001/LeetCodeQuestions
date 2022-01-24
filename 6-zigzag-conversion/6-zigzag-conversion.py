class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i = 0
        row = 0
        length = len(s)
        res = ['' for i in range(numRows)]
        while(i<length):
            try:
                for j in range(numRows):
                    res[j] += s[i]
                    i += 1
                for j in range(numRows -2,0,-1):
                    res[j] += s[i]
                    i += 1
            except:
                break
        return ''.join(res)
                