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


class Solution:
    """
    Optimal solution with O(1) space complexity
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        # Use the first cell of each row and col to mark as filling 0 or not
        # After traversing, we do not know wether first column have a 0 from the beginning or not
        has_zero_in_first_col = False
        for r in range(rows):
            if matrix[r][0] == 0:
                has_zero_in_first_col = True

            # Traverse from second column, if we meet a 0
            # Mark the first cells of current row and col as 0
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = matrix[0][c] = 0

        # Traverse from bottom-right to fill the 0s
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, 0, -1):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
            if has_zero_in_first_col:
                matrix[r][0] = 0
