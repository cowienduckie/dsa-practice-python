from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Turn the array into a min heap
        ans = 0
        heapify(nums)
        # Because the constraints make sure that there is always an answer
        # Loop until the smallest one in heap no smaller than k
        while nums[0] < k:
            x, y = heappop(nums), heappop(nums)
            heappush(nums, x * 2 + y)
            ans += 1
        return ans
