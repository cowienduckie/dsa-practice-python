from typing import List


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        rows, cols = len(coins), len(coins[0])
        dp = [[[0] * 3 for _ in range(cols)] for _ in range(rows)]

        for r in range(1, rows):
            dp[r][-1] = [float("-inf")] * 3
        for c in range(1, cols):
            dp[-1][c] = [float("-inf")] * 3

        for r in range(rows):
            for c in range(cols):
                dp[r][c][2] = max(
                    dp[r - 1][c][1],
                    dp[r][c - 1][1],
                    dp[r - 1][c][2] + coins[r][c],
                    dp[r][c - 1][2] + coins[r][c],
                )
                dp[r][c][1] = max(
                    dp[r - 1][c][0],
                    dp[r][c - 1][0],
                    dp[r - 1][c][1] + coins[r][c],
                    dp[r][c - 1][1] + coins[r][c],
                )
                dp[r][c][0] = max(dp[r - 1][c][0], dp[r][c - 1][0]) + coins[r][c]

        return max([dp[rows - 1][cols - 1][k] for k in range(3)])
