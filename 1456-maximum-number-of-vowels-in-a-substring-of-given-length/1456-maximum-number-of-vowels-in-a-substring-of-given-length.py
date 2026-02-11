class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = set("aeiou")
        count = 0
        for i in range(k):
            if s[i] in v:
                count += 1
        max_count = count
        for i in range(k, len(s)):
            if s[i - k] in v:
                count -= 1
            if s[i] in v:
                count += 1
            max_count = max(max_count, count)
        return max_count