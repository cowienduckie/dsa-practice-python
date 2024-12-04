from collections import deque
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # Pop all interval cannot overlap new one
        ans = []
        queue = deque(intervals)
        while queue and queue[0][1] < newInterval[0]:
            ans.append(queue.popleft())

        # Merge all possible overlapping
        overlapping = newInterval
        while queue:
            interval = queue.popleft()
            if interval[0] <= overlapping[1] and interval[1] >= overlapping[0]:
                overlapping = [
                    min(overlapping[0], interval[0]),
                    max(overlapping[1], interval[1]),
                ]
            else:
                ans.append(overlapping)
                overlapping = interval
        ans.append(overlapping)

        return ans
