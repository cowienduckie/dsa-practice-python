class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if r < m - 1:
                    dp[r + 1][c] += dp[r][c]
                if c < n - 1:
                    dp[r][c + 1] += dp[r][c]

        return dp[m - 1][n - 1]
