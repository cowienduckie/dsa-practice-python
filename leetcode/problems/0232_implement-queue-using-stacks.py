class MyQueue:

    def __init__(self):
        # s1 has the elements in the order old -> new
        # s2 has the elements in the order new -> old
        self.s1 = list()
        self.s2 = list()

    def push(self, x: int) -> None:
        if self.s2:
            while self.s2:
                self.s1.append(self.s2.pop())
        self.s1.append(x)

    def pop(self) -> int:
        if self.s1:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if self.s1:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2
