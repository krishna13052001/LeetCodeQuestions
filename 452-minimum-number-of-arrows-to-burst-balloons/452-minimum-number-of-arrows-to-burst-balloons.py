class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if(len(points)<2):
            return len(points)
        points.sort(key=lambda x : x[1])
        count = 1
        end = points[0][1]
        i = 1
        print(points)
        while(i<len(points)):
            if(end < points[i][0]):
                count += 1
                end = points[i][1]
            i += 1
        return count