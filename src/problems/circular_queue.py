class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.items = 0
        self.head = 0
        self.tail = 0
        self.array = [-1] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.items += 1
        self.array[self.tail] = value
        if self.tail == self.k-1:
            self.tail = 0
        else:
            self.tail += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.array[self.head] = -1
        self.items -= 1
        if self.head == self.k - 1:
            self.head = 0
        else:
            self.head += 1
        return True

    def Front(self) -> int:
        return self.array[self.head]

    def Rear(self) -> int:
        return self.array[self.tail-1]

    def isEmpty(self) -> bool:
        return self.items == 0

    def isFull(self) -> bool:
        return self.items == self.k


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
print(obj.enQueue(1))
print(obj.enQueue(2))
print(obj.enQueue(3))
print(obj.enQueue(4))
print(obj.Rear())
print(obj.isFull())
print(obj.deQueue())
print(obj.enQueue(4))
print(obj.Rear())
