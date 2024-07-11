class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        temp = ""
        for i in s:
            if i != ")":
                stack.append(i)
            elif len(stack) > 0:
                temp = ""
                ele = stack.pop()
                while ele != "(":
                    temp += ele
                    ele = stack.pop()
                for el in temp:
                    stack.append(el)
        temp = ""
        for ele in stack:
            temp += ele
        return temp
        