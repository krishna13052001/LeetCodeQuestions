class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x : x[1])
        last_short = float("-inf")
        count = 0
        for point in points:
            if last_short >= point[0]:
                continue
            last_short = point[1]
            count += 1
        return count