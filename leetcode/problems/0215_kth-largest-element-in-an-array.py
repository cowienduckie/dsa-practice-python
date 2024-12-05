from heapq import heapify, heappop
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
        heapify(nums)
        for _ in range(k - 1):
            heappop(nums)

        return heappop(nums) * -1
