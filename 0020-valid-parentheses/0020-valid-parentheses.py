class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        d = {"(":True, "[": True, "{": True}
        for char in s:
            if d.get(char, False):
                temp.append(char)
            else:
                if len(temp) == 0:
                    return False
                ele = temp.pop()
                if char == ")":
                    if ele != '(':
                        return False
                elif char == "]":
                    if ele != '[':
                        return False
                elif char == "}":
                    if ele != "{":
                        return False
        if len(temp) > 0:
            return False
        return True