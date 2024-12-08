from bisect import bisect_right
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)

        # Sort events by end time and store the end times separately
        events.sort(key=lambda x: x[1])
        ending = [end for _, end, _ in events]

        # Store the best value at each end time
        memo = [events[0][2]] * n
        for i in range(1, n):
            memo[i] = max(memo[i - 1], events[i][2])

        # Find the answer using binary search for best value before each start time
        # If an event has no before-event, just take only it to compare
        ans = 0
        for start, _, value in events:
            i = bisect_right(ending, start - 1)
            if i > 0:
                ans = max(ans, value + memo[i - 1])
            else:
                ans = max(ans, value)

        return ans
