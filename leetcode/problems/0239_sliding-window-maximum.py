from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Store the indices of the sliding window's numbers in a monotonic decreasing queue
        # The largest number in queue is always at the queue's front at each step
        n = len(nums)
        queue = deque()
        ans = list()

        for i in range(n):
            # Pop the front numbers if they're out of the window
            while queue and queue[0] < i - k + 1:
                queue.popleft()

            # Pop the back numbers if they're smaller than the new number
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            # Append the largest number in the queue to the answer
            if i >= k - 1:
                ans.append(nums[queue[0]])
        return ans
