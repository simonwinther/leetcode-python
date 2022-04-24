from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.sum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        if len(self.queue) > self.size:
            self.sum -= self.queue.popleft()
        self.sum += val
        return self.sum / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
print(obj.next(1))  # return 1.0 = 1 / 1
print(obj.next(10))  # return 5.5 = (1 + 10) / 2
print(obj.next(3))  # return 4.66667 = (1 + 10 + 3) / 3
print(obj.next(5))  # return 6.0 = (10 + 3 + 5) / 3
