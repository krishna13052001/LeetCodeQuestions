class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word_lst = list(word)
        for idx, letter in enumerate(word_lst):
            if letter == ch:
                word_lst[0:idx+1] = word_lst[0:idx+1][::-1]
                break
        
        return "".join(word_lst)