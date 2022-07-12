class MinStack:

    def __init__(self):
        self.stack = []
        self.index = 0
        self.min = 0

    def push(self, val: int) -> None:
        if(self.index == 0):
            self.stack.append(val)
            self.min = val
        else:
            if(val<self.min):
                self.stack.append(2 * val - self.min)
                self.min = val
            else:
                self.stack.append(val)
        self.index += 1

    def pop(self) -> None:
        if(self.index <= 0):
            return
        self.index -= 1
        value = self.stack.pop()
        if(value < self.min):
            self.min = 2*self.min - value

    def top(self) -> int:
        if(self.index <= 0):
            return
        value = self.stack[self.index-1]
        if(value < self.min):
            return self.min
        return value

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()