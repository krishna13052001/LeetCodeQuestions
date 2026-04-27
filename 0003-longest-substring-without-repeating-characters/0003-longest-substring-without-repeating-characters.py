from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)
        left = right = 0
        result = 0
        while right < len(s):
            if s[right] not in d:
                d[s[right]] += 1
                result = max(result, right - left + 1)
                right += 1
            else:
                d[s[left]] -= 1
                if d[s[left]] == 0:
                    del d[s[left]]
                left += 1
        return result
