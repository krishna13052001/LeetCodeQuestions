class TrieNode:
    def __init__(self):
        self.ended = False
        self.children = {}
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.ended = True
    

    def search(self, word: str) -> bool:
        return self.__search(word, self.root)

    def __search(self, word, cur):
        if not word:
            return cur.ended

        w = word[0]
        if w != ".":
            if w in cur.children:
                return self.__search(word[1:], cur.children[w])
            else:
                return False
        else:
            for child in cur.children.values():
                if self.__search(word[1:], child):
                    return True

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)