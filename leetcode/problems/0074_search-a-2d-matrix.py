from typing import List, Tuple


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        def to_matrix_index(pos: int) -> Tuple[int, int]:
            return (pos // cols, pos % cols)

        left, right = 0, rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            (row, col) = to_matrix_index(mid)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
