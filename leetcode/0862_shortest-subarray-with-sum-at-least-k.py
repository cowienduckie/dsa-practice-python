from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n, ans = len(nums), float("inf")

        # Compute prefix sum for each element
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Maintain a deque to store the index of prefix sum
        queue = deque()
        for i in range(n + 1):
            # Try to shrink the sub-array by removing leftmost positive numbers
            while queue and prefix[i] - prefix[queue[0]] >= k:
                ans = min(ans, i - queue.popleft())

            # Try to shrink the sub-array by removing rightmost numbers to keep the queue is increasing
            while queue and prefix[i] <= prefix[queue[-1]]:
                queue.pop()

            # Append the index of prefix sum to the deque
            queue.append(i)

        return ans if ans != float("inf") else -1


nums = [2, -1, 2, -1, -3, 1]
k = 3
print(Solution().shortestSubarray(nums, k))
