from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        # Store all coordinates of cells into a dictionary
        memo = {}
        for r in range(rows):
            for c in range(cols):
                memo[mat[r][c]] = (r, c)

        # Use 2 arrays to track filled cells by row and col
        row_check = [cols] * rows
        col_check = [rows] * cols
        for i, num in enumerate(arr):
            r, c = memo[num]
            row_check[r] -= 1
            col_check[c] -= 1
            # Return the smallest index where a row or col is fully filled
            if not row_check[r] or not col_check[c]:
                return i
        return -1
