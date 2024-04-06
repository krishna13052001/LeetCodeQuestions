class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = ""
        invalid_paranthesis = 0
        open_parantheisis_count = 0
        for idx in range(len(s)):
            if s[idx] == "(":
                invalid_paranthesis += 1
                open_parantheisis_count += 1
                ans += s[idx]
            elif s[idx] == ")":
                if invalid_paranthesis == 0:
                    continue
                invalid_paranthesis -= 1
                ans += s[idx]
            else:
                ans += s[idx]
        res = ""
        open_parantheisis_count -= invalid_paranthesis
        for i in range(len(ans)):
            if ans[i] == "(":
                open_parantheisis_count -= 1
                if open_parantheisis_count < 0 :
                    continue
            res += ans[i]
        return res
                
                    