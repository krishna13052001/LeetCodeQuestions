from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        wordlist = set(wordList)
        queue = deque([(beginWord, 1)])
        while queue:
            word, distance = queue.popleft()
            if word == endWord:
                return distance
            for i in range(len(word)):
                for j in range(27):
                    if j != ord(word[i]) - ord("a"):
                        new_word = word[:i] + chr(ord("a") + j) + word[i+1:]
                        if new_word in wordlist:
                            queue.append((new_word, distance + 1))
                            wordlist.remove(new_word)
        return 0
                    