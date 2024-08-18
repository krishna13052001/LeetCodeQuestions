class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        sorted_pairs = sorted(pairs, key= lambda x:x[1])
        count = 0
        last_interval = float("-inf")
        for pair in sorted_pairs:
            if pair[0] > last_interval:
                count += 1
                last_interval = pair[1]
        return count