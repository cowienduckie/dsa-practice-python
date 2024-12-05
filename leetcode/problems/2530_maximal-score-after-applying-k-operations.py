import heapq
from math import ceil
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-1 * x for x in nums]
        heapq.heapify(max_heap)
        ans = 0
        while k > 0:
            curr_max = -1 * heapq.heappop(max_heap)
            ans = ans + curr_max
            heapq.heappush(max_heap, -1 * ceil(curr_max / 3))
            k = k - 1
        return ans
