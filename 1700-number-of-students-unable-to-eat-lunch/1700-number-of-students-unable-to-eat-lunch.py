class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        d = {1:0, 0:0}
        for i in students:
            if i == 1:
                d[i] += 1
            elif i == 0:
                d[i] += 1
        
        for i in sandwiches:
            if d[i] > 0:
                d[i] -= 1
            else:
                return d[1] + d[0]
        return 0