from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        For n x n matrix, rotating the matrix by 90 degrees is equivalent to swapping the values of 4 cells:
        (i, j) -> (j, n - 1 - i) -> (n - 1 - i, n - 1 - j) -> (n - 1 - j, i) -> (i, j)

        So we only need to iterate through the top-left quarter of the matrix:
        - For odd n, the quarters are rectangles with a single cell in the middle
        - For even n, the quarters are squares
        """

        n = len(matrix)
        rows = n // 2
        cols = n // 2 + (1 if n % 2 else 0)

        for i in range(rows):
            for j in range(cols):
                (
                    matrix[i][j],
                    matrix[j][n - 1 - i],
                    matrix[n - 1 - i][n - 1 - j],
                    matrix[n - 1 - j][i],
                ) = (
                    matrix[n - 1 - j][i],
                    matrix[i][j],
                    matrix[j][n - 1 - i],
                    matrix[n - 1 - i][n - 1 - j],
                )
