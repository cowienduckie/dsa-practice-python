from collections import defaultdict
from heapq import heappop, heappush


class NumberContainers:
    def __init__(self):
        # Store indices of a same number in a heap
        self.indices = defaultdict(list)
        # Store the container by index
        self.container = {}

    def change(self, index: int, number: int) -> None:
        # Add number into container's index
        self.container[index] = number
        # Add index into number's indices heap
        heappush(self.indices[number], index)

    def find(self, number: int) -> int:
        # Check if number has no index
        if number not in self.indices or not self.indices[number]:
            return -1
        # Lazy deletion of replaced indices of finding number
        while (
            self.indices[number] and self.container[self.indices[number][0]] != number
        ):
            heappop(self.indices[number])
        # Return the smallest index of the number
        return self.indices[number][0] if self.indices[number] else -1
