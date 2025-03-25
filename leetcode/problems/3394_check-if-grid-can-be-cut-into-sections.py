from typing import List, Tuple


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # Check for valid cuts in both horizontal and vertical directions
        horizontal = [(start, end) for start, _, end, _ in rectangles]
        vertical = [(start, end) for _, start, _, end in rectangles]

        return self._can_divide(horizontal) or self._can_divide(vertical)

    def _can_divide(self, segments: List[Tuple[int, int]]) -> bool:
        # Sort all segments by starting point
        segments.sort(key=lambda seg: seg[0])
        pos = 0

        # Find first division
        pos = self._find_next_division(segments, pos)

        # Find second division
        pos = self._find_next_division(segments, pos)

        # Check if there are segments after second division
        return pos < len(segments)

    def _find_next_division(
        self, segments: List[Tuple[int, int]], start_pos: int
    ) -> int:
        # Early exit if there are no segments left
        if start_pos >= len(segments):
            return start_pos

        # Take the first segment as the division point
        division = segments[start_pos][1]
        pos = start_pos + 1

        # Find the all segments that overlap with the division
        while pos < len(segments) and segments[pos][0] < division:
            division = max(division, segments[pos][1])
            pos += 1

        return pos


print(
    Solution().checkValidCuts(
        4, [[0, 0, 1, 4], [1, 0, 2, 3], [2, 0, 3, 3], [3, 0, 4, 3], [1, 3, 4, 4]]
    )
)
