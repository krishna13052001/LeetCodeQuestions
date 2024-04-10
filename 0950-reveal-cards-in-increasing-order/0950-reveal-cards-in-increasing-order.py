from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        length = len(deck)
        q = deque()
        ans = [0] * length
        for i in range(length):
            q.append(i)
        
        for i in range(length):
            try:
                top = q.popleft()
                ans[top] = deck[i]
                if len(q) > 0:
                    q.append(q.popleft())
            except Exception as e:
                print(e)
        return ans