from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        zero_rows = [False] * rows
        zero_cols = [False] * cols

        for r in range(rows):
            for c in range(cols):
                if not matrix[r][c]:
                    zero_rows[r] = True
                    zero_cols[c] = True

        for r in range(rows):
            for c in range(cols):
                if zero_rows[r] or zero_cols[c]:
                    matrix[r][c] = 0
