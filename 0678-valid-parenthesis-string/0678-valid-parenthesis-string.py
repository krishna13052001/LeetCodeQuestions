class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for i in s:
            if i == "(":
                leftMin += 1
                leftMax += 1
            elif i == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            if leftMax < 0:
                return False
            leftMin = max(leftMin, 0)
        return leftMin == 0