class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        idx = 0
        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            res.append(intervals[idx])
            idx += 1
        while idx < len(intervals) and intervals[idx][0] <= newInterval[1]:
            newInterval[0] = min(intervals[idx][0], newInterval[0])
            newInterval[1] = max(intervals[idx][1], newInterval[1])
            idx += 1
        res.append(newInterval)
        while idx < len(intervals):
            res.append(intervals[idx])
            idx += 1
        return res

        