from collections import Counter 
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxFreq = max(freq.values())
        maxCount = sum(1 for f in freq.values() if f == maxFreq)
        part_len = (maxFreq - 1) * (n + 1) + maxCount
        return max(len(tasks), part_len)