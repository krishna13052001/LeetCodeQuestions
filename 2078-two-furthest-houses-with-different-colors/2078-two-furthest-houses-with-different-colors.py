class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        n = len(colors)
        j = n - 1
        while colors[j] == colors[0]:
            j -= 1
        i = 0
        while colors[i] == colors[-1]:
            i += 1
        return max(j - 0, n - 1 - i)