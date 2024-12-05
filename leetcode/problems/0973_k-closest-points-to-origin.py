from heapq import heappop, heappush
from typing import List


class Solution:
    """
    Solution using Heap
    """

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            heappush(heap, (p[0] * p[0] + p[1] * p[1], p))

        ans = []
        for _ in range(k):
            ans.append(heappop(heap)[1])

        return ans


class Solution:
    """
    Sorter solution using built-in sort function
    """

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0] * p[0] + p[1] * p[1])
        return points[:k]


class Solution:
    """
    Sorter solution using built-in sorted function
    """

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x: x[0] * x[0] + x[1] * x[1])[:k]
