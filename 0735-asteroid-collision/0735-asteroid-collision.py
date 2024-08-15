class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        n = len(asteroids)
        for i in range(n):
            if len(stack) == 0 or asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                while(len(stack) > 0 and stack[-1] > 0 and stack[-1] < abs(asteroids[i])):
                    stack.pop()
                
                if len(stack) > 0 and stack[-1] == abs(asteroids[i]):
                    stack.pop()
                else:
                    if(len(stack) ==0 or stack[-1] < 0):
                        stack.append(asteroids[i])
        return stack
