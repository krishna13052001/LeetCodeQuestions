import bisect
class ExamRoom:

    def __init__(self, n: int):
        self.size = n
        self.seats = []
        self.first = -1

    def seat(self) -> int:
        if(self.first == -1):
            idx = 0
            self.first = 0
        else:
            res, idx = 0,0
            ans = self.seats[0] - 0
            if(ans > res):
                res = ans
                idx = 0
            for j in range(len(self.seats)-1):
                i = (self.seats[j] + self.seats[j+1]) // 2
                ans = min(abs(self.seats[j] - i), abs(self.seats[j+1] - i))
                if ans > res:
                    res = ans
                    idx = i
            ans = self.size-1 - self.seats[-1]
            if ans > res:
                res = ans
                idx = self.size-1
        bisect.insort(self.seats,idx)
        return idx

    def leave(self, p: int) -> None:
        self.seats.remove(p)
        if(len(self.seats) == 0):
            self.first = -1


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)