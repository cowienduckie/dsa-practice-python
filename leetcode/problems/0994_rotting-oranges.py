from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))

        ans = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                if row + 1 < rows and grid[row + 1][col] == 1:
                    queue.append((row + 1, col))
                    grid[row + 1][col] = 2

                if row - 1 >= 0 and grid[row - 1][col] == 1:
                    queue.append((row - 1, col))
                    grid[row - 1][col] = 2

                if col + 1 < cols and grid[row][col + 1] == 1:
                    queue.append((row, col + 1))
                    grid[row][col + 1] = 2

                if col - 1 >= 0 and grid[row][col - 1] == 1:
                    queue.append((row, col - 1))
                    grid[row][col - 1] = 2
            if queue:
                ans += 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1

        return ans
