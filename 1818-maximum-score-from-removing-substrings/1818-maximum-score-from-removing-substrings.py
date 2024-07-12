class Solution:
    def points(self, s, sub, point):
        totalpoints = 0
        n = len(s)
        stack = []
        for i in range(n):
            if len(stack) == 0:
                stack.append(s[i])
            else:
                if s[i] == sub[1] and stack[-1] == sub[0]:
                    stack.pop()
                    totalpoints += point
                else:
                    stack.append(s[i])
        s = ""
        while len(stack) > 0:
            s += stack.pop()
        s = s[::-1]
        return totalpoints, s
    def swap(self, a, b):
        temp = a
        a = b
        b = temp
        return a, b
    def maximumGain(self, s: str, x: int, y: int) -> int:
        s1 = "ab"
        s2 = "ba"
        if x < y:
            s1, s2 = self.swap(s1,s2)
            x, y = self.swap(x,y)
        point, new_s = self.points(s, s1, x)
        point2, new_s = self.points(new_s, s2, y)
        return  point + point2