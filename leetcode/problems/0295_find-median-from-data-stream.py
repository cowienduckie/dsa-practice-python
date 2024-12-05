from heapq import heappop, heappush


class MedianFinder:

    def __init__(self):
        self.min_heap = []  # Min-heap for the larger half of numbers
        self.max_heap = []  # Max-heap for the smaller half of numbers

    def addNum(self, num: int) -> None:
        # Add the number to the appropriate heap
        if self.min_heap and num > self.min_heap[0]:
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, -num)

        # Balance the heaps if their sizes differ by more than 1
        if len(self.min_heap) > len(self.max_heap) + 1:
            heappush(self.max_heap, -heappop(self.min_heap))
        elif len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))

    def findMedian(self) -> float:
        # Calculate the median based on the sizes of the heaps
        if len(self.min_heap) > len(self.max_heap):
            return float(self.min_heap[0])
        elif len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        else:  # Both heaps are of equal size
            return (self.min_heap[0] - self.max_heap[0]) / 2.0
