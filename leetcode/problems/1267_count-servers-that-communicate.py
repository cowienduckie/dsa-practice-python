from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # Count the number of servers in each row and column
        row_count = [0] * rows
        col_count = [0] * cols
        total_servers = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1
                    total_servers += 1

        # Count the number of servers cannot communicate with any other servers
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and row_count[r] == 1 and col_count[c] == 1:
                    total_servers -= 1
        return total_servers
