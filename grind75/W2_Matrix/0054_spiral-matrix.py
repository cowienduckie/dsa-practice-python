from typing import List, Optional, Tuple


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        ans = list()

        def get_next_cell(
            row: int, col: int, direction: int
        ) -> Optional[Tuple[int, int]]:
            if direction == 0:  # Go right
                next_row, next_col = row, col + 1
            elif direction == 1:  # Go down
                next_row, next_col = row + 1, col
            elif direction == 2:  # Go left
                next_row, next_col = row, col - 1
            else:  # Go up
                next_row, next_col = row - 1, col

            return (
                (next_row, next_col)
                if 0 <= next_row < rows
                and 0 <= next_col < cols
                and matrix[next_row][next_col] is not None
                else None
            )

        def traverse(row: int, col: int, direction: int) -> None:
            ans.append(matrix[row][col])
            matrix[row][col] = None

            # If we can't move in the current direction, change direction once and try again
            # If we can't move in the new direction, we reached the end of the matrix
            for _ in range(2):
                next_cell = get_next_cell(row, col, direction)

                if next_cell:
                    return traverse(next_cell[0], next_cell[1], direction)
                else:
                    direction = (direction + 1) % 4  # Change direction

        traverse(0, 0, 0)
        return ans
