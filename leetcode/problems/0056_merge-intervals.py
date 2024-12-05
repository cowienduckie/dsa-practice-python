from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        overlapping = intervals[0]
        ans = []

        for interval in intervals:
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
