import math


class MinStack:

    def __init__(self):
        self.ptr = 0
        self.min = None
        self.data = []

    def push(self, val: int) -> None:
        if self.min is None:
            self.min = val
        elif val < self.min:
            self.min = val
        self.data.append(val)

    def pop(self) -> None:
        if self.data[len(self.data) - 1] == self.min:
            self.data.pop()
            self.min = math.inf
            for i in range(len(self.data)):
                if self.data[i] < self.min:
                    self.min = self.data[i]
        else:
            self.data.pop()

    def top(self) -> int:
        return self.data[len(self.data) - 1]

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
