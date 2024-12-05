from typing import List


class Solution:
    """
    Use sets to store the presence of numbers in rows, columns, and boxes.
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = [set() for _ in range(9)]
        col_check = [set() for _ in range(9)]
        box_check = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif (
                    board[i][j] in row_check[i]
                    or board[i][j] in col_check[j]
                    or board[i][j] in box_check[i // 3][j // 3]
                ):
                    return False

                row_check[i].add(board[i][j])
                col_check[j].add(board[i][j])
                box_check[i // 3][j // 3].add(board[i][j])
        return True


class Solution2:
    """
    Use bit manipulation to store the presence of numbers in rows, columns, and boxes.
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = [0] * 9
        col_check = [0] * 9
        box_check = [[0] * 3 for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                num = int(board[i][j])
                bitmask = 1 << num

                if (
                    row_check[i] & bitmask
                    or col_check[j] & bitmask
                    or box_check[i // 3][j // 3] & bitmask
                ):
                    return False

                row_check[i] |= bitmask
                col_check[j] |= bitmask
                box_check[i // 3][j // 3] |= bitmask
        return True


class Solution3:
    """
    Use boolean arrays to store the presence of numbers in rows, columns, and boxes.
    Somehow, this version is the best on both runtime and memory among the three on LeetCode.
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = [[False] * 9 for _ in range(9)]
        col_check = [[False] * 9 for _ in range(9)]
        box_check = [[[False] * 9 for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                num = int(board[i][j]) - 1
                if (
                    row_check[i][num]
                    or col_check[j][num]
                    or box_check[i // 3][j // 3][num]
                ):
                    return False

                row_check[i][num] = True
                col_check[j][num] = True
                box_check[i // 3][j // 3][num] = True
        return True
