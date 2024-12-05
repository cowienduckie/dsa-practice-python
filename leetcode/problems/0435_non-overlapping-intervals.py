from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Using greedy algorithm by sorting by end time, and always choose the interval with the earliest end time
        intervals.sort(key=lambda x: x[1])
        curr_end = float("-inf")
        ans = len(intervals)

        # For each interval is not overlapping with the previous one, we have no need to remove it
        for start, end in intervals:
            if start >= curr_end:
                curr_end = end
                ans -= 1
        return ans
