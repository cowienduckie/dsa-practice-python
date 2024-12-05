class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.head = None
        self.tail = None
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.head = 0
            self.tail = 0
            self.queue[0] = value
        else:
            self.tail = (self.tail + 1) % self.size
            self.queue[self.tail] = value

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        if self.head == self.tail:  # Only one element in the queue
            self.head = None
            self.tail = None
        else:
            self.head = (self.head + 1) % self.size

        return True

    def Front(self) -> int:
        return self.queue[self.head] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.queue[self.tail] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.head == None

    def isFull(self) -> bool:
        return not self.isEmpty() and (self.tail + 1) % self.size == self.head
