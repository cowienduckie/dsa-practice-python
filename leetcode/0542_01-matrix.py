from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        queue = deque()  # row, col

        for row in range(rows):
            for col in range(cols):
                if mat[row][col]:
                    mat[row][col] = float("inf")
                else:
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()

            if row + 1 < rows and mat[row + 1][col] > mat[row][col] + 1:
                queue.append((row + 1, col))
                mat[row + 1][col] = mat[row][col] + 1

            if row - 1 >= 0 and mat[row - 1][col] > mat[row][col] + 1:
                queue.append((row - 1, col))
                mat[row - 1][col] = mat[row][col] + 1

            if col + 1 < cols and mat[row][col + 1] > mat[row][col] + 1:
                queue.append((row, col + 1))
                mat[row][col + 1] = mat[row][col] + 1

            if col - 1 >= 0 and mat[row][col - 1] > mat[row][col] + 1:
                queue.append((row, col - 1))
                mat[row][col - 1] = mat[row][col] + 1

        return mat
