from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Split the original matrix into 4 quarters around the center and rotate them clockwise following below order:
        (r, c) -> (c, n - 1 - r) -> (n - 1 - r, n - 1 - c) -> (n - 1 - c, r) -> (r, c)
        """

        # Base case
        n = len(matrix)
        if n == 1:
            return

        # Calculate dimension sizes of 4 quarters
        rows = n // 2
        cols = n // 2 + (n & 1)

        # Rotate 4 quarters clockwise around center of the matrix
        for r in range(rows):
            for c in range(cols):
                (
                    matrix[r][c],
                    matrix[c][n - 1 - r],
                    matrix[n - 1 - r][n - 1 - c],
                    matrix[n - 1 - c][r],
                ) = (
                    matrix[n - 1 - c][r],
                    matrix[r][c],
                    matrix[c][n - 1 - r],
                    matrix[n - 1 - r][n - 1 - c],
                )
