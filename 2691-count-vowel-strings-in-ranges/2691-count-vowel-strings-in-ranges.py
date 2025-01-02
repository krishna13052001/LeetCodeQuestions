class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_sum = [0] * (len(words) + 1)
        vowels = ['a', 'e', 'i', 'o', 'u']
        for idx, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                prefix_sum[idx+1] = 1 + prefix_sum[idx]
            else:
                prefix_sum[idx+1] = prefix_sum[idx]
        res = []
        for query in queries:
            res.append(prefix_sum[query[1]+1] - prefix_sum[query[0]])
        return res