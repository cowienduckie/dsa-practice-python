from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0 if x else 1 for x in range(cols)] for _ in range(rows)]

        ans = 1
        for col in range(1, cols):
            for row in range(rows):
                for prev_row in range(row - 1, row + 2):
                    if (
                        0 <= prev_row < rows
                        and grid[row][col] > grid[prev_row][col - 1]
                        and dp[prev_row][col - 1]
                    ):
                        dp[row][col] = max(dp[row][col], dp[prev_row][col - 1] + 1)

                ans = max(ans, dp[row][col])

        return ans - 1
