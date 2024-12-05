class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # Use 2D-matrix to store max length of palindrome in subseq from i to j
        # Base cases:
        # - If i > j, then dp[i][j] = 0
        # - If i = j, then dp[i][j] = 1
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    # If the range [i, j] has s[i] same as s[j], lengthen range (i, j) by 2
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # Otherwise, range [i, j] equal to max of [i, j) or (i, j]
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
