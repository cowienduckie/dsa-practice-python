from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = 0

        def dfs(row: int, col: int) -> None:
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == "1":
                grid[row][col] = "0"

                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    ans += 1

        return ans
