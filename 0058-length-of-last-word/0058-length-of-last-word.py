class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        prevCount = 0
        for i in s:
            if i == " ":
                if count != 0:
                    prevCount = count
                count = 0
            else:
                count += 1
        if count == 0:
            return prevCount
        return count