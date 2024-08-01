class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for s in details:
            if int(s[11:13]) > 60:
                ans += 1
        return ans