class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[1])
        count = 0
        last_interval = float("-inf")
        for interval in intervals:
            if interval[0] >= last_interval:
                last_interval = interval[1]
            else:
                count += 1
        return count