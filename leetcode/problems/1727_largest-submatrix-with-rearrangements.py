from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        ans = 0

        # Convert original matrix to heights of histogram with baseline at each row
        for r in range(rows):
            for c in range(cols):
                if r > 0 and matrix[r][c]:
                    matrix[r][c] += matrix[r - 1][c]
            # For each row, sort the heights descending and compute the max area of histogram
            ans = max(ans, self._computeMaxArea(sorted(matrix[r], reverse=True)))

        return ans

    def _computeMaxArea(self, arr: List[int]) -> int:
        max_area = arr[0]
        for i in range(1, len(arr)):
            max_area = max(max_area, min(arr[i], arr[i - 1]) * (i + 1))
        return max_area
