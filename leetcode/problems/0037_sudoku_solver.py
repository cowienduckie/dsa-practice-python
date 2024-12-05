from typing import List, Tuple


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Use backtracking to try all possible numbers for each cell.
        If one solution is found, return True to exit recursion.
        """

        def get_valid_numbers(row: int, col: int) -> List[str]:
            # Check existing numbers in row and col
            existing = set()
            for i in range(9):
                existing.add(board[row][i])
                existing.add(board[i][col])

            # Check existing numbers in sub-boxes
            top_left_row = (row // 3) * 3
            top_left_col = (col // 3) * 3
            for i in range(3):
                for j in range(3):
                    existing.add(board[top_left_row + i][top_left_col + j])

            # Return the leftovers from 1 to 9
            valid = list()
            for i in range(1, 10):
                if not str(i) in existing:
                    valid.append(str(i))

            return valid

        def solve(row: int, col: int) -> bool:
            nonlocal board
            # If the sudoku is done, return True to exit recursion
            if row == 9:
                return True

            next_row, next_col = (row + 1, 0) if col == 8 else (row, col + 1)

            # If the current cell is already filled, go to next cells
            if board[row][col] != ".":
                return solve(next_row, next_col)

            # If there is no valid numbers for this cell, return False
            valid_numbers = get_valid_numbers(row, col)
            if not valid_numbers:
                return False

            # Fill the current cell with valid numbers and go to next cells
            for num in valid_numbers:
                board[row][col] = num
                if solve(next_row, next_col):
                    return True
                board[row][col] = "."

        solve(0, 0)


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],  # 1 2 4 6 8 9
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
Solution().solveSudoku(board=board)
print(board)
