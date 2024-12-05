from heapq import heappop, heappush
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        min_heap = []
        for key, val in freq_dict.items():
            heappush(min_heap, (val, key))
            if len(min_heap) > k:
                heappop(min_heap)

        return [key for _, key in min_heap]
