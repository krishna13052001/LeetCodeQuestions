class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i in range(len(s)):
            d[s[i]] = i
        print(d)
        size = end = 0
        res = []
        for i in range(len(s)):
            size += 1
            end = max(end, d[s[i]])
            if i == end:
                res.append(size)
                size = 0
        return res
            