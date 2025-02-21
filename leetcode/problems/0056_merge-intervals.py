from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals ascending
        intervals.sort(key=lambda x: x[0])

        # Append a dummy interval in the last to complete checking after one loop
        intervals.append([float("inf"), float("inf")])

        # Iterate through intervals and merging the overlapping
        ans = []
        overlap_start, overlap_end = intervals[0]

        for i in range(1, len(intervals)):
            # Extract start and end time of current interval
            start, end = intervals[i]

            # If current interval do not overlap with the overlapping ones, push the overlapping into answers
            # Otherwise, merge current end time with the overlapping
            if start > overlap_end:
                ans.append([overlap_start, overlap_end])
                overlap_start, overlap_end = start, end
            else:
                overlap_end = max(overlap_end, end)

        return ans
