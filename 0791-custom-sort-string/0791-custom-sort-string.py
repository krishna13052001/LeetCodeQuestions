class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {}
        for i in s:
            if freq.get(i,-1) == -1:
                freq[i] = 1
            else:
                freq[i] += 1
        res = ""
        for i in order:
            if freq.get(i,-1) != -1:
                res += (i * freq[i])
                del freq[i]
        for key in list(freq.keys()):
            res += (key * freq[key])
        return res