class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []

        def sub_string(i):
            if i >= len(s):
                result.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.is_pali(s, i, j):
                    part.append(s[i:j + 1])
                    sub_string(j + 1)
                    part.pop()

        sub_string(0)
        return result

    def is_pali(self, str, l, r):
        while l < r:
            if str[l] != str[r]:
                return False
            l, r = l + 1, r - 1
        return True
