from collections import deque
from typing import List


class Solution:
    """
    Solution using built-in deque
    """

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


class Solution:
    """
    Solution only using loops and array
    """

    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        new_start, new_end = newInterval
        # Find the start of combined interval
        for start, end in intervals:
            if start <= new_start <= end:
                new_start = min(new_start, start)
                break
        # Find the end of combined interval
        for start, end in intervals:
            if start <= new_end <= end:
                new_end = max(new_end, end)
                break

        # Push all intervals that end before the combined interval
        i, result = 0, []
        while i < len(intervals):
            if intervals[i][1] < new_start:
                result.append(intervals[i])
                i += 1
            else:
                break
        # Push the combined interval
        result.append([new_start, new_end])

        # Push all intervals that end after the combined interval
        while i < len(intervals):
            if intervals[i][0] > new_end:
                result.append(intervals[i])
            i += 1

        return result
