from collections import deque
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        stack = deque(sorted(people))
        count = 0
        while(stack):
            end = stack.pop()
            count += 1
            if(stack and end + stack[0]<=limit):
                stack.popleft()
        return count