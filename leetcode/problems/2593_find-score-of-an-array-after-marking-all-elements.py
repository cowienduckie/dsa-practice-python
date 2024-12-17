from heapq import heapify, heappop
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        marked = [False] * len(nums)

        # Use a min heap to get the smallest number
        heap = [(num, i) for i, num in enumerate(nums)]
        heapify(heap)

        while heap:
            curr_min, index = heappop(heap)

            # Check if current index is marked yet
            if marked[index]:
                continue

            marked[index] = True
            if index + 1 < len(nums):
                marked[index + 1] = True
            if index - 1 >= 0:
                marked[index - 1] = True

            # Update score
            score += nums[index]

        return score
