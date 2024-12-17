from cmath import sqrt
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-1 * x for x in gifts]
        heapify(heap)
        for _ in range(k):
            heappush(heap, -1 * int(sqrt(-1 * heappop(heap))))

        return -1 * sum(heap)
