from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num, i) for i, num in enumerate(nums)]
        heapify(heap)

        for _ in range(k):
            _, i = heappop(heap)
            nums[i] *= multiplier
            heappush(heap, (nums[i], i))

        return nums
