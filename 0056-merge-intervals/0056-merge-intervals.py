class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals,key = lambda x:x[0])
        ans = []
        res = []
        for interval in sorted_intervals:
            if len(ans) == 0 or ans[1] < interval[0]:
                res.append(interval)
                ans = interval
            elif ans[1] >= interval[0]:
                ans = res.pop()
                res.append([ans[0], max(ans[1], interval[1])])
                ans = res[-1]
        return res