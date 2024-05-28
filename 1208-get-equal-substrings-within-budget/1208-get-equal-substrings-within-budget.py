class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        lst = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        i, j, ans, cur_sum = 0, 0, 0, 0

        while j < len(lst):
            cur_sum += lst[j]
            if cur_sum <= maxCost:
                ans = max(ans, j - i + 1)
            else:
                while cur_sum > maxCost:
                    cur_sum -= lst[i]
                    i += 1
            j += 1
        
        return ans